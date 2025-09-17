# src/planner.py
from langchain_openai import ChatOpenAI
from typing import List

class QueryPlanner:
    def __init__(self, api_key: str):
        self.llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=api_key)

    def generate_subqueries(self, query: str) -> List[str]:
        prompt = f"""
        Break down the following research question into 2–4 sub-queries 
        that can be independently retrieved from a research paper database.

        Question: {query}

        Return only the sub-queries as a list, no explanation.
        """
        response = self.llm.invoke(prompt)
        subqueries = response.content.strip().split("\n")
        return [sq.strip("- ").strip() for sq in subqueries if sq.strip()]
