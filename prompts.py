from langchain_core.prompts import ChatPromptTemplate
from knowledge_base import company_info
from parser import parser

format_instructions = parser.get_format_instructions()

support_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are TechStore's professional AI Customer Support Assistant.

Below is the company information:

{company_info}

Rules:
1. Answer politely.
2. Never make up information.
3. If you don't know the answer, say:
"I'm sorry, I don't have that information."
4. Return ONLY valid JSON.

{format_instructions}
"""
        ),
        (
            "human",
            "{question}"
        )
    ]
).partial(
    company_info=company_info,
    format_instructions=format_instructions
)