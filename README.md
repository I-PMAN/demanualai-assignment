🚀 AI-Powered LinkedIn Post Generator

This project is an AI-powered API service that uses Google Gemini API + LangChain to fetch recent news on a given topic and generate a LinkedIn-style post in a professional and engaging tone.

📌 Features

Fetches recent news articles on any topic using Serper (Google Search API).

Summarizes and generates a LinkedIn-style post using Google Gemini.

Provides sources used for transparency.

Includes optional image suggestion placeholder.

FastAPI backend with Swagger UI for testing.

Deployed on Vercel for easy access.

⚙️ Setup Instructions

1. Clone the repository
 ```
git clone https://github.com/I-PMAN/demanualai-assignment.git
cd demanualai-assignment
``` 
2. Create a virtual environment
```
python3 -m venv .venv
source .venv/bin/activate
```
3. Install dependencies
```
pip install -r requirements.txt
```
4. Set up environment variables
```
Create a .env file in the root folder:
API_KEY=your_gemini_api_key
SERPER_KEY=your_serper_api_key
```
5. Run locally
```
uvicorn main:app --reload
```

Open Swagger docs at: http://127.0.0.1:8000/docs

🖥️ API Usage
Endpoint
```
POST /generate-post
```

Input (JSON)
```
{
  "topic": "Artificial Intelligence"
}
```

Example Response
```
{
  "topic": "Artificial Intelligence",
  "news_sources": [
    "https://example.com/article1",
    "https://example.com/article2",
    "https://example.com/article3"
  ],
  "linkedin_post": "Artificial Intelligence continues to transform industries ...",
  "image_suggestion": null
}
```

🌐 Live Swagger API

👉 Hosted Swagger Docs
