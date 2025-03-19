from langchain.agents import AgentExecutor
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.agents.openai_functions_agent.base import create_openai_functions_agent
from langchain_core.prompts import ChatPromptTemplate

# 가짜 데이터베이스
fake_db = {
    "John": {"age": 30, "location": "Seoul"},
    "Alice": {"age": 25, "location": "Busan"}
}

@tool
def fake_api_lookup(name: str) -> str:
    """가짜 API를 통해 사용자 정보를 조회합니다.
    
    Args:
        name (str): 사용자 이름
        
    Returns:
        str: 사용자 정보 또는 오류 메시지
    """
    if name in fake_db:
        user_info = fake_db[name]
        return f"{name}님의 정보: 나이 {user_info['age']}, 위치 {user_info['location']}"
    else:
        return f"{name}님의 정보를 찾을 수 없습니다."

# LLM 및 에이전트 설정
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{input}"),
    ("assistant", "{agent_scratchpad}")
])

tools = [fake_api_lookup]
agent = create_openai_functions_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 실행
if __name__ == "__main__":
    result = agent_executor.invoke({"input": "내 이름은 'John'이야. 내 정보를 조회해줘."})
    print(result["output"])