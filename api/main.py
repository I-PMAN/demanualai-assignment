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

    topic = request.topic
    articles = get_articles(topic)

    urls = [a.get("link") for a in articles.get("organic", [])[:3]]

    ai_query = (
            f"Using the following sources {urls}, write a LinkedIn-style post"
            f"summarizing the latest news about '{topic}'."
            "Keep it professional and engaging."
            "End with a thought-provoking note."
            "Do not include extra text outside the post."
    )

    response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[ai_query]
    )

    linkedin_post = response.candidates[0].content.parts[0].text

    return {
            "toppic" : topic,
            "news_sources" : urls,
            "linkedin_post" : linkedin_post,
            "image_suggestion" : None
            }

def get_articles(topic):
    os.environ["SERPER_API_KEY"] = os.getenv("SERPER_KEY")
    search = GoogleSerperAPIWrapper()
    query = f"latest 3 news articles about {topic}"
    return search.results(query)
