# src/critic.py
from langchain_openai import ChatOpenAI

class Critic:
    def __init__(self, api_key: str, model: str = "gpt-4o-mini"):
        self.llm = ChatOpenAI(model=model, temperature=0, api_key=api_key)

    def review_answer(self, query: str, draft_answer: str) -> str:
        """
        Critic reviews the synthesized answer, checking for:
        - Consistency across sources
        - Conflicts / contradictions
        - Missing perspectives
        Returns a refined final answer.
        """
        prompt = f"""
        You are an academic Critic Agent. Review the following draft answer
        for the query: "{query}"

        Draft Answer:
        {draft_answer}

        Your tasks:
        1. Identify if there are any contradictions or inconsistencies.
        2. Point out missing perspectives if any.
        3. Refine the draft into a polished academic answer (structured, clear, factual).
        
        Provide the improved final answer below:
        """
        response = self.llm.invoke(prompt)
        return response.content.strip()