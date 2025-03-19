from langchain.agents import AgentExecutor
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.agents.openai_functions_agent.base import create_openai_functions_agent
from langchain_core.prompts import ChatPromptTemplate

# 내부 "가짜 API"를 모방한 Tool 정의
@tool
def fake_api_greet(name: str) -> str:
    """사용자 이름을 받아 환영 메시지를 반환하는 가짜 API를 호출합니다.
    
    Args:
        name (str): 사용자 이름
        
    Returns:
        str: 환영 메시지
    """
    # 내부적으로 API 호출을 흉내내는 로직
    greeting = f"안녕하세요, {name}님! 환영합니다."
    return greeting

# LLM 및 에이전트 설정
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)  # gpt-4 대신 gpt-3.5-turbo 사용 가능
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{input}"),
    ("assistant", "{agent_scratchpad}")
])

# Tool 등록
tools = [fake_api_greet]
agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 에이전트 실행
if __name__ == "__main__":
    result = agent_executor.invoke({"input": "내 이름은 'John'이야. 나를 환영해줘."})
    print(result["output"])