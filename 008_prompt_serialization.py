from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from pydantic import BaseModel, Field


class Movie(BaseModel):
    title: str = Field(description="The title of the movie")
    year: int = Field(description="The year the movie was released")
    rating: float = Field(description="The rating of the movie")


parser = PydanticOutputParser(pydantic_object=Movie)

format_instructions = parser.get_format_instructions()

# {}가 python에서 변수로 해석되니까 이스케이프 처리
format_instructions = (
    parser.get_format_instructions().replace("{", "{{").replace("}", "}}")
)


# # 프롬프트 템플릿에 format_instructions를 직접 포함시킴
prompt = PromptTemplate(
    template="{subject}에 대한 영화를 랜덤으로 생성해줘.\n" + format_instructions,
    input_variables=["subject"],
)

# # 저장
prompt.save("prompt.json")


# 로드
from langchain.prompts import load_prompt

my_prompt = load_prompt("prompt.json")
# print(my_prompt.invoke({"subject": "코딩"}))

from langchain_openai import ChatOpenAI

llm = ChatOpenAI()
chain = my_prompt | llm | parser

print(chain.invoke({"subject": "코딩"}))