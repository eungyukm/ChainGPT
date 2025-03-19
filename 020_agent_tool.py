from langchain.tools import tool

@tool
def my_tool(input: str) -> str:
    """설명: 입력을 받아 변환한 후 반환"""
    return input[::-1]  # 문자열 뒤집기

print(my_tool("안녕하세요"))