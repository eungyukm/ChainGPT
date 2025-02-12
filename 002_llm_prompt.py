from langchain.prompts import PromptTemplate

prompt = PromptTemplate.from_template("Translate the following into {language}: {text}")
res = prompt.format(language="Korean", text="Hello, I'm Aiden.")


from langchain.prompts import ChatPromptTemplate

template = "Translates {input_language} to {output_language}"
human_message = "{text}"

chat_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", template),
        ("human", human_message),
    ]
)

res = chat_prompt.format_messages(
    input_language="English",
    output_language="Korean",
    text="Hello, I'm Aiden.",
)


from langchain_openai import ChatOpenAI

chat_model = ChatOpenAI(model="gpt-4o-mini")
chat_model_output = chat_model.invoke(res)
print(type(chat_model_output))
print(chat_model_output)