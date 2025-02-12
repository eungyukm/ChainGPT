from langchain.prompts import PromptTemplate

# 프롬프트 만들기

prompt = PromptTemplate.from_template("나에게 {subject}에 대한 유머를 말해줘")

# print(prompt.invoke({"subject": "고양이"}))

# parser 만들기
from langchain.schema import BaseOutputParser, StrOutputParser


class CommaSeparatedListOutputParser(BaseOutputParser):
    def parse(self, text: str) -> list:
        return text.strip().split(",")


parser = StrOutputParser()


# 모델 가져오기
from langchain_openai import ChatOpenAI

llm = ChatOpenAI()

# LCEL Chain 만들고 실행하기

chain = prompt | llm | parser
print(chain.invoke({"subject": "양자역학"}))