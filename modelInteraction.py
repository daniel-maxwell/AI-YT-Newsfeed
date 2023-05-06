# Set the environment variable
import os
os.environ["OPENAI_API_KEY"] = "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" # OpenAi API key
os.environ["GOOGLE_CSE_ID"] = "b5ff08ee5e6314b12" # Google custom search engine ID
os.environ["GOOGLE_API_KEY"] = "AIzaSyCqVHWQmsaFLkOQGgKrOlYL4LPqAYqsZhk" # Google API key

# Import the LLM wrapper
from langchain.llms import OpenAI

# Construct prompt templates
from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

# Import agent prerquisites
from langchain.agents import load_tools
from langchain.agents.load_tools import get_all_tool_names
from langchain.agents import initialize_agent
from langchain.agents import AgentType
from langchain.utilities import GoogleSearchAPIWrapper
#from langchain import ConversationChain

# Set model temperature
llm = OpenAI(temperature=0)

# List available tools
# print(get_all_tool_names())

# Load tools
tools = load_tools(["google-search", "llm-math"], llm=llm)
search = GoogleSearchAPIWrapper(k=10) # Pass in number of results to return

# Initialize the  agent with the tools and the LLM
agent = initialize_agent(
    tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

# Generates the correct template depending on whether the user specified any portfolio focuses, e.g. ESG investing
def constructTemplate(age, investment_goal, risk_profile, budget, focuses):
    if len(focuses) == 0:
        promptTemplate = f'''Create the best passive investment portfolio for the user based on their requirements.
                            The response should be a list of each investment in the portfolio and the number of dollars per month to allocate to that investment.
                            The user is {age} years old with a monthly budget of {budget}. The goal of the portfolio should be {investment_goal} with a {risk_profile} risk profile.
                        '''
    
    if len(focuses) == 1:
        promptTemplate = f'''You must create an investment portfolio adhering to the following requirements.
                            The target is {age} years old with a maximum monthly budget of {budget}. The goal of the portfolio should be {investment_goal} with a {risk_profile} risk profile. The focus of the portfolio should be {focuses[0]} investing.
                            Respond with a list of ticker symbols for each investment in your suggested portfolio and the monthly budget allocation to each investment in dollars.
                        '''
        
    return promptTemplate


# User requirements. Manually set for now, but we will present the user with a form to collect this information
Age=25
Investment_Goal="retirement"
Risk_Profile="medium"
Budget=1000
focusSelections = ["ESG"]

# Create the template
template = constructTemplate(Age, Investment_Goal, Risk_Profile, Budget, focusSelections)

# Create a PromptTemplate instance, passing in the template we created
prompt = PromptTemplate(
    input_variables=[],
    template=template,
)

# Check that the prompt was constructed correctly.
#print(prompt)

agent.run(prompt)