from langchain_google_genai import ChatGoogleGenerativeAI
from config import GEMINI_API_KEY
from prompts import support_prompt

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GEMINI_API_KEY,
)


def chat_with_ai(question):
    chain = support_prompt | llm

    response = chain.invoke(
        {
            "question": question
        }
    )

    return response.content 