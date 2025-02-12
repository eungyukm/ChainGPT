from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings()

# single text
text = "안녕하세요"
res = embeddings.embed_query(text)
print(len(res))
print(res)

# multiple text
texts = ["안녕하세요", "반갑습니다"]
res = embeddings.embed_documents(texts)
print(res)