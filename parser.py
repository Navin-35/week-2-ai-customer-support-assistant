from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel


class SupportResponse(BaseModel):
    category: str
    answer: str


parser = JsonOutputParser(pydantic_object=SupportResponse)