from langchain.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI

# loader
loader = PyPDFLoader("data/ground_rule.pdf")
data_list = loader.load_and_split()

template = (
    "너는 내 비서야, 다음의 {document_data}문서를 참고해서 {query}에 대해 답변해줘"
)
user_message = "5가지 룰이 뭐야?"
chat_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", template),
        ("human", user_message),
    ]
)

res = chat_prompt.format_messages(query=user_message, document_data=data_list)
# print(res)  # prompt 형식으로 변환

llm = ChatOpenAI()

chain = chat_prompt | llm

llm_res = chain.invoke({"query": user_message, "document_data": data_list})
content = llm_res.content
print(content)