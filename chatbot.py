from langchain_google_genai import ChatGoogleGenerativeAI
from config import GEMINI_API_KEY
from prompts import support_prompt
from parser import parser

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GEMINI_API_KEY,
)

chain = support_prompt | llm | parser


def chat_with_ai(question):
    return chain.invoke(
        {
            "question": question
        }
    )