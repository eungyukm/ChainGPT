from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="data/movies.csv")
docs = loader.load()

# print(type(docs))
# print(docs)
print(type(docs[0]))
print(docs[0].page_content)