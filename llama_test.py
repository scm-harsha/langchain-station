from langchain.llms import Ollama
from langchain.agents import load_tools, initialize_agent, AgentType


def llm_func(input):
    llm = Ollama(model="llama2")
    return llm(input)


def starcoder_func(input):
    llm = Ollama(model="starcoder")
    return llm(input)


def langchain_agent(input):
    llm = Ollama(model="llama2")
    tools = load_tools(["llm-math", "wikipedia"], llm=llm)
    agent = initialize_agent(
        tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True
    )
    return agent.run(input)
