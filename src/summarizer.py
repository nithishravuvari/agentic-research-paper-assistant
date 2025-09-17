# src/summarizer.py
from langchain_openai import ChatOpenAI
from langchain.schema import Document
from typing import List

class Summarizer:
    def __init__(self, api_key: str):
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=api_key)

    def summarize_docs(self, docs: List[Document], subquery: str) -> str:
        joined_text = "\n\n".join([doc.page_content for doc in docs])
        prompt = f"""
        Summarize the following research snippets in the context of:
        "{subquery}"

        Text:
        {joined_text}

        Provide a concise academic-style summary (3–4 sentences).
        """
        response = self.llm.invoke(prompt)
        return response.content.strip()
