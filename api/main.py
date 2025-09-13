from fastapi import FastAPI
from google import genai
from dotenv import load_dotenv
import os
import pprint
from langchain_community.utilities import GoogleSerperAPIWrapper
import json
from pydantic import BaseModel

load_dotenv()
app = FastAPI()

class PostRequest(BaseModel):
    topic: str

@app.post("/generate-post")
def generate_post(request: PostRequest):
    gemini_api_key = os.getenv("API_KEY")
    client = genai.Client(api_key=gemini_api_key)
    result = {}
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="",
    )
    topic = request.topic
    articles = get_articles(topic)

    urls = []
    for article in articles["organic"]:
        urls.append(article["link"])
    result["topic"] = topic
    result["news_sources"] = urls
    ai_query = f"Use the top 3 sources and generate a LinkedIn-style post for the topic {topic} summarizing the news in {result}. The tone of the post should be professional and engaging. Do not add any extra text in the response."
    response = client.models.generate_content(
            model="gemini-2.5-flash",
    contents=ai_query)
    
    linkedin_post = response.candidates[0].content.parts[0].text
    result["linkedin_post"] = linkedin_post
    return{"response" : result}


def get_articles(topic):
    os.environ["SERPER_API_KEY"] = os.getenv("SERPER_KEY")
    search = GoogleSerperAPIWrapper()
    query = f"Give me a list of 3 latest news or articles with sources for the topic {topic}. Also include an image suggestion if possible."
    result = search.results(query)
    return result
