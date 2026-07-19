from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage
from config import GEMINI_API_KEY
from prompts import support_prompt
from parser import parser

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=GEMINI_API_KEY,
)

history = []


def chat_with_ai(question):
    chain = support_prompt | llm | parser

    response = chain.invoke({
        "question": question
    })

    history.append(HumanMessage(content=question))
    history.append(AIMessage(content=response["answer"]))

    return response


def clear_history():
    history.clear()