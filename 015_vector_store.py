from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.document_loaders import CSVLoader
from langchain_openai import OpenAIEmbeddings

# Data Load
loader = CSVLoader(file_path="data/shopping.csv")
whole_data = loader.load()
# print(whole_data)

# Split
splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
split_data = splitter.split_documents(whole_data)
# print(split_data[0])

# Embedding
embeddings = OpenAIEmbeddings()

# Vector Store
vector_store = Chroma.from_documents(
    documents=split_data,
    embedding=embeddings,
    persist_directory="my_vector_store",
)