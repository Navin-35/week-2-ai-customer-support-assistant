from langchain_google_genai import ChatGoogleGenerativeAI
from config import GEMINI_API_KEY

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GEMINI_API_KEY,
)


def chat_with_ai(message):
    response = llm.invoke(message)
    return response.content