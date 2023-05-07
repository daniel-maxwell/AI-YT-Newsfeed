# Load the environment
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# Load langchain modules
from langchain.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import find_dotenv, load_dotenv
from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
import textwrap

embeddings = OpenAIEmbeddings()

# Outputs a searchable database from the transcript of a YT video 
def create_db_from_youtube_urls(video_urls):
    transcripts = []
    for url in video_urls:
        loader = YoutubeLoader.from_youtube_url(url)
        transcripts.extend(loader.load())

    # Split transcript in to a list of documents
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(transcripts)

    # Uses embeddings to convert split documents in to a vector (numerical) representation
    # Then, uses FAISS to create a db that can be used for efficient similarity search
    db = FAISS.from_documents(docs, embeddings)
    return db


# gpt-3.5-turbo can handle up to 4097 tokens. Setting the chunksize to 1000 and k to 4 maximizes
# the number of tokens to analyze.
def get_response_from_query(db, query, k=4):

    docs = db.similarity_search(query, k=k)
    docs_page_content = " ".join([d.page_content for d in docs])

    chat = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.2)

    # Template to use for the system message prompt
    template = """
        You are a journalist that writing a magazine article based on video transcripts: {docs}
        
        Only use the factual information from the transcripts to write the article.

        Your answer should be verbose and as detailed as possible, like a front page magazine article.
        """

    system_message_prompt = SystemMessagePromptTemplate.from_template(template)

    # Human question prompt
    human_template = "{question}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)

    chat_prompt = ChatPromptTemplate.from_messages(
        [system_message_prompt, human_message_prompt]
    )

    chain = LLMChain(llm=chat, prompt=chat_prompt)

    response = chain.run(question=query, docs=docs_page_content)
    response = response.replace("\n", "")
    return response, docs


# Example usage:
video_urls = ["https://www.youtube.com/watch?v=L_Guz73e6fw", "https://www.youtube.com/watch?v=qpoRO378qRY", "https://www.youtube.com/watch?v=Gfr50f6ZBvo"]
db = create_db_from_youtube_urls(video_urls)

query = "What is an interesting development or discussion happening in the field of AI?"
response, docs = get_response_from_query(db, query)
print(textwrap.fill(response, width=50))