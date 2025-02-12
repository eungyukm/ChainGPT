from langchain.prompts import ChatPromptTemplate
from langchain_chroma import Chroma
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

url = "https://namu.wiki/w/리그 오브 레전드/챔피언/역할군"
loader = WebBaseLoader(
    web_paths=(url,),
)
docs = loader.load()
# print(docs)

text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
splits = text_splitter.split_documents(docs)
# print(splits)

embeddings = OpenAIEmbeddings()
vector_store = Chroma.from_documents(
    documents=splits,
    embedding=embeddings,
    persist_directory="my_vector_store",
)

retriever = vector_store.as_retriever()


prompt = ChatPromptTemplate.from_template(
    """
당신은 리그 오브 레전드 챔피언 역할군에 대한 정보를 제공하는 봇입니다.
검색된 다음 문맥을 사용하여 질문에 답하세요.
답을 모른다면 모른다고 말하세요.
답변은 최대 세 문장으로 간결하게 작성하세요.

Question: {question}
Context: {context}
Answer: """
)

question = input("🦊 질문: ")
print(f"🦊 질문: {question}")

docs = retriever.invoke(question)
context = "\n".join([doc.page_content for doc in docs])

llm = ChatOpenAI(model="gpt-4o-mini")

chain = prompt | llm
res = chain.invoke({"context": context, "question": question})
print(f"🤖 답변: {res.content}")