# AI Youtube Newsfeed

The aim of this project is to create an application that utilizes the LangChain framework to create news feed articles based on information gathered from youtube videos. This application demonstrates the power of combining language models with custom data and leveraging various modules provided by LangChain. This application is currently under development and is not in an MVP state.

## How it Works

1. **Document Loading:** The application uses the LangChain document loader specifically designed for YouTube videos to retrieve the transcript based on a given video URL.
2. **Text Splitting:** The transcript is split into smaller chunks, each containing a maximum of 1000 tokens, using the LangChain text splitter module. This step ensures that the transcript can be processed within the token limit imposed by the language model.
3. **Embeddings and Vector Database:** The application converts the split transcript chunks into numerical representations called factors using the embeddings module. These factors are then stored in a vector database using the phase library for efficient similarity search.
4. **User Queries:** Users can ask questions about the video transcript by inputting their queries into the application.
5. **Similarity Search:** The application performs a similarity search on the vector database to identify the most relevant transcript chunks based on the user's query.
6. **Language Model Interaction:** The relevant transcript chunks are combined into a single string and used as input to the GPT 3.5 turbo language model through the LangChain chat module.
7. **Prompt Generation:** The application generates a prompt that instructs the language model to provide a response based on the given query and the content of the relevant transcript chunks.
8. **Response Generation:** The language model generates a response based on the prompt and the available information from the transcript. The response is then returned to the user.

## Current Features (This section will be updated with each commit)

- Retrieval of YouTube video transcript based on a list of video URLs.
- Splitting of the transcripts into smaller chunks to fit within the token limit.
- Use of Meta's FAISS library to create of a vector database containing numerical representations of the transcript chunks.
- GPT writes an article based on some of the information gathered from the video transcripts.

## Getting Started

To run the LangChain YouTube Transcript Assistant locally, follow these steps:

1. Clone the LangChain repository from [GitHub](https://github.com/langchain/langchain).
2. Install the required dependencies using `pip` or your preferred package manager.
3. Set up the necessary API keys and environment variables as described in the LangChain documentation.
4. Run the application using your preferred Python IDE or the command line.


## Limitations

- The transcript chunks may not cover the entire content of the video, resulting in potential gaps in the responses.
- The accuracy of the responses depends on the quality and accuracy of the original transcript.
- The application relies on the availability and accessibility of YouTube video transcripts. If a transcript is not available or cannot be retrieved, the application will not be able to generate responses.
- The language model's responses are based solely on the information present in the transcript. Responses may be misleading or entirely false based on the videos passed in.
- The application is currently limited to YouTube video transcripts as the data source. Integrating other document loaders and data sources is a goal I would like to work towards.

## Future Enhancements

The LangChain YouTube Transcript Assistant provides a foundation for further development and enhancements. Here are some potential areas for improvement:

- Improved Transcript Retrieval: Enhance the document loader to handle cases where video transcripts are not readily available or use alternative methods to obtain the transcript.
- Expanded Data Sources: Extend the application to support other data sources beyond YouTube, such as podcasts, interviews, or conference proceedings. Implement additional document loaders accordingly.
- Advanced Prompt Engineering: Explore more sophisticated prompt generation techniques to extract specific information from the transcript, allowing for more accurate and targeted responses.
- User Interface: Develop a user-friendly web interface where users can input video URLs, view responses, and explore transcript details conveniently.
- Natural Language Processing: Incorporate natural language processing techniques to enhance the understanding of user queries and improve response accuracy.
- Integration with External APIs: Integrate with external APIs, such as search engines or knowledge bases, to enrich the information available for answering user queries.
- Continuous Training: Keep the language model up-to-date by periodically retraining it with new and relevant data to ensure the accuracy and relevance of responses.

## License

The LangChain YouTube Transcript Assistant is open-source software licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to fork, modify, and contribute to the project.

## Acknowledgments

The LangChain framework and the YouTube Transcript Assistant build upon the advancements in natural language processing and machine learning made possible by organizations such as OpenAI and Facebook Research. I acknowledge their contributions to the field and the availability of their tools and libraries for building innovative applications.