from fastapi import FastAPI
import openai
import os

app = FastAPI()

openai.api_key = os.getenv("OPENAI_API_KEY")

