from langchain.schema import BaseOutputParser


class CommaSeparatedListOutputParser(BaseOutputParser):
    def parse(self, text: str) -> list:
        return text.strip().split(",")


parser = CommaSeparatedListOutputParser()

print(parser.invoke("a, b, c"))