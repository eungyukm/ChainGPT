from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field


class Movie(BaseModel):
    title: str = Field(description="The title of the movie")
    year: int = Field(description="The year the movie was released")
    rating: float = Field(description="The rating of the movie")


parser = PydanticOutputParser(pydantic_object=Movie)
# print(parser.get_format_instructions())

temperature = 0.0
model_name = "gpt-4o-mini"
llm = ChatOpenAI(temperature=temperature, model_name=model_name)


prompt = PromptTemplate.from_template(
    template="{subject}에 대한 영화를 랜덤으로 생성해줘.\n{format_instructions}",
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

chain = prompt | llm | parser

movie = chain.invoke({"subject": "코딩"})
print(movie.title)
print(movie.year)
print(movie.rating)