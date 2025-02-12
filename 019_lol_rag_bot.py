import pyfiglet
from langchain.prompts import ChatPromptTemplate
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

# 기존 임베딩된 데이터 활용
embeddings = OpenAIEmbeddings()
vector_store = Chroma(
    persist_directory="my_vector_store", embedding_function=embeddings
)

# 벡터 DB가 비어 있는지 체크
if not vector_store._collection.count():
    print("⚠️ 기존 벡터 DB에 데이터가 없습니다. 먼저 임베딩을 수행하세요.")
else:
    print("✅ 기존 벡터 DB를 불러왔습니다.")

print(pyfiglet.figlet_format("Sparta LoL Bot"))

retriever = vector_store.as_retriever()

prompt = ChatPromptTemplate.from_template(
    """
당신은 리그 오브 레전드 챔피언 역할군에 대한 정보를 제공하는 봇입니다.
검색된 다음 문맥을 사용하여 질문에 답하세요.
답을 모른다면 모른다고 말하세요.
답변은 최대 세 문장으로 간결하게 작성하세요.
친절하게 대답해주세요.

Question: {question}
Context: {context}
Answer: """
)

# 사용자 입력 받기
question = input("🦊 질문: ")

# 벡터 DB에서 관련 문서 검색
docs = retriever.invoke(question)
context = "\n".join([doc.page_content for doc in docs])

# LLM 설정
llm = ChatOpenAI(model="gpt-4o-mini")

# RAG 실행
chain = prompt | llm
res = chain.invoke({"context": context, "question": question})

print(f"🤖 답변: {res.content}")