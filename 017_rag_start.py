from langchain.prompts import ChatPromptTemplate
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

# embeddings
embeddings = OpenAIEmbeddings()

# vector store
vector_store = Chroma(
    persist_directory="my_vector_store",
    embedding_function=embeddings,
)

# retriever
retriever = vector_store.as_retriever()

# LLM
llm = ChatOpenAI(model="gpt-4o-mini")

# prompt
prompt = ChatPromptTemplate.from_template(
    """
당신은 질문 답변 작업의 보조자입니다.
검색된 다음 문맥을 사용하여 질문에 답하세요.
답을 모른다면 모른다고 말하세요.
답변은 최대 세 문장으로 간결하게 작성하세요.

Question: {question}
Context: {context}
Answer: """
)

# question
question = "하얀색 제품은 어떤 것이 있나요?"
print(f"🦊 질문: {question}")

# retrieved docs
retrieved_docs = retriever.invoke(question)

# context
context = "\n".join([doc.page_content for doc in retrieved_docs])

# chain
chain = prompt | llm
res = chain.invoke({"context": context, "question": question})
print(f"🤖 답변: {res.content}")