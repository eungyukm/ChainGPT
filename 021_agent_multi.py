from langchain.agents import AgentExecutor
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.agents.openai_functions_agent.base import create_openai_functions_agent
from langchain_core.prompts import ChatPromptTemplate

@tool
def reverse_string(text: str) -> str:
    """입력된 문자열을 뒤집습니다."""
    return text[::-1]

@tool
def to_upper_case(text: str) -> str:
    """입력된 문자열을 대문자로 변환합니다."""
    return text.upper()

llm = ChatOpenAI(model="gpt-4", temperature=0)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{input}"),
    ("assistant", "{agent_scratchpad}")
])

tools = [reverse_string, to_upper_case]
agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 실행 및 출력
result = agent_executor.invoke({"input": "LangChain을 대문자로 변환하고 뒤집어줘."})
print(result["output"])  # 중복 방지를 위해 output만 출력