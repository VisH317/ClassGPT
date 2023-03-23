from fastapi import FastAPI
import openai
import os

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.get("/question")
def answerQuestion(question: str = ""):
    # setup an assistant for later
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "prompt": "You are a question answering assistant who answers questions posed by students, but you do not give the answer directly and instead guide the question asker to a plausible answer"},
            {"role": "user", "prompt": question}
        ]
    )

    return response['choices']['content']

@app.get("/info")
def provideInfo(start: str = ""):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "prompt": "You are an assistant that provides more information based on a given prompt. You use the provided information to find more related information to provide as an output. The input will contain just the base text that needs to be expanded upon"},
            {"role": "user", "prompt": start}
        ]
    )

    return response['choices']['content']