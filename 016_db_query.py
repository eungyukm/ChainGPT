from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

# db conn
embeddings = OpenAIEmbeddings()
vector_store = Chroma(
    persist_directory="my_vector_store",
    embedding_function=embeddings,
)

# Query
my_query = "하얀색"
docs = vector_store.similarity_search(my_query)
# print(docs[0].page_content)


retriever = vector_store.as_retriever()
docs = retriever.invoke(my_query)
print(docs[0].page_content)