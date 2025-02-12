from langchain_community.document_loaders import JSONLoader

file_path = "data/chat.json"
loader = JSONLoader(
    file_path=file_path,
    jq_schema=".[]",  # 배열의 각 항목을 개별적으로 가져옴
    text_content=False,  # JSON 객체 형태 유지
)

documents = loader.load()
print(documents)