from fastapi import FastAPI
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()

@app.post("/generate-post")
def generate_post():
    return {"Hello" : "World"}

@app.get("/")
def app_root():
    gemini_api_key = os.getenv("API_KEY")
    print(gemini_api_key)
    client = genai.Client(api_key=gemini_api_key)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Explain how a car works in a 100 words",
    )

    return{"response":response.text}
