from langchain.tools import tool

@tool
def calculate(expression: str) -> float:
    """수식을 계산합니다."""
    try:
        return eval(expression)
    except Exception as e:
        return f"오류 발생: {e}"

# 테스트
print(calculate("2 + 3 * 5"))  # 17