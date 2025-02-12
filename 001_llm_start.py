from dotenv import load_dotenv
from langchain_openai import OpenAI

load_dotenv()

llm = OpenAI()

input_text = "안녕하세요. 저는 에이든입니다."

print(llm.invoke(input_text))
print("---")


from langchain.schema import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
chat_model = ChatOpenAI()
messages = [
    SystemMessage(content="you are a helpful assistant"),
    HumanMessage(content=input_text),
]

print(chat_model.invoke(messages))