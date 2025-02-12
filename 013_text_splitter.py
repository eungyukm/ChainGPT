from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=10, chunk_overlap=5)

text = "동해 물과 백두산이 마르고 닳도록 하느님이 보우하사 우리나라 만세"
len(text)

# 문자열 리스트 List[str]
print(text_splitter.split_text(text))

#  LangChain Document 객체 리스트 List[Document]
print(text_splitter.create_documents([text]))