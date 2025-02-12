import os
import sys

import pyfiglet
from dotenv import load_dotenv

ascii_art = pyfiglet.figlet_format("LLM + LangChain")
print(f"\n{ascii_art}")

try:
    import langchain
    import langchain_community
    import langchain_core
    import langchain_openai
    import numpy
    import openai
    import pydantic

    print("\n 필수 라이브러리 로드 성공!\n")

except ImportError as e:
    print(f"라이브러리 로드 실패: {e}")
    sys.exit(1)

# 🔍 LangChain 버전 체크
print(f"📌 ✅ LangChain 버전: {langchain.__version__}\n")

# Load .env file
if "OPENAI_API_KEY" in os.environ:
    del os.environ["OPENAI_API_KEY"]
load_dotenv(override=True)

# 🔑 OpenAI API 키 확인
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    print("⚠️  OPENAI_API_KEY 환경 변수가 설정되지 않았습니다.")
    print("   ➜ export OPENAI_API_KEY='your_openai_api_key'")
    sys.exit(1)
else:
    print("🔑 ✅ OPENAI API 키 확인됨\n")

from langchain.schema import HumanMessage

# 📖 LangChain LLM 테스트
from langchain_openai import ChatOpenAI

try:
    llm = ChatOpenAI()
    messages = [HumanMessage(content="What is LangChain?")]
    response = llm.invoke(messages)
    print("🤖 ✅ LLM 응답 테스트 성공 (", response.content[:30], "...)\n")

except Exception as e:
    print(f"❌ LangChain 실행 실패: {e}")
    sys.exit(1)

print("LangChain 환경 설정 완료!")