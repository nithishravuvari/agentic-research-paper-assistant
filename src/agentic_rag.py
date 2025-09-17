# src/agentic_rag.py

import os
from dotenv import load_dotenv
from src.planner import QueryPlanner
from src.rag_pipeline import retrieve_docs
from src.summarizer import Summarizer
from src.critic import Critic
from src.formats import format_answer
from langchain_openai import ChatOpenAI

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def run_agentic_rag(query: str, mode: str = "detailed") -> dict:
    """
    Run the Agentic RAG pipeline.
    Modes:
      - "concise"     → short structured summary
      - "detailed"    → full structured explanation
      - "comparison"  → output suitable for tabular comparison
    Returns a dict with keys:
      - "content" : str
      - "references" : list of str
    """

    # 1. Planner
    planner = QueryPlanner(api_key=OPENAI_API_KEY)
    subqueries = planner.generate_subqueries(query)
    # print("\n[Planner] Sub-queries:", subqueries)

    # 2. Retrieve + summarize
    summarizer = Summarizer(api_key=OPENAI_API_KEY)
    sub_summaries = []
    references = []

    for sq in subqueries:
        docs = retrieve_docs(sq, k=3)
        summary = summarizer.summarize_docs(docs, sq)
        sub_summaries.append(f"**{sq}**\n{summary}")

        for d in docs:
            title = d.metadata.get("title", "Unknown Title")
            authors = d.metadata.get("authors", [])
            if isinstance(authors, (list, tuple)):
                authors_str = ", ".join(str(a).strip() for a in authors)
            else:
                authors_str = str(authors).strip()
            references.append(f"{title} | {authors_str}")

    # 3. Final synthesis (mode-aware prompt)
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=OPENAI_API_KEY)

    if mode == "concise":
        synthesis_prompt = f"""
        You are an academic assistant. Merge the following sub-summaries into a
        **concise, structured answer** to the original question.
        Keep it short, focusing only on key points.
        Use bullet points or very brief sections.

        Question: {query}
        Sub-summaries:
        {'\n\n'.join(sub_summaries)}
        """
    elif mode == "comparison":
        synthesis_prompt = f"""
        You are an academic assistant. Merge the following sub-summaries into a
        **comparison-style output**. Use a clear table (Markdown format) to compare
        the key aspects, challenges, and advances side by side.

        Question: {query}
        Sub-summaries:
        {'\n\n'.join(sub_summaries)}
        """
    else:  # detailed (default)
        synthesis_prompt = f"""
        You are an academic assistant. Merge the following sub-summaries into a
        **detailed, coherent structured answer** to the original question.
        Use sub-headings, paragraphs, and examples when appropriate.

        Question: {query}
        Sub-summaries:
        {'\n\n'.join(sub_summaries)}
        """

    draft_answer = llm.invoke(synthesis_prompt).content.strip()

    # 4. Critic Review
    critic = Critic(api_key=OPENAI_API_KEY)
    reviewed_answer = critic.review_answer(query, draft_answer)

    # 5. Format output (always unified dict)
    answer_dict = format_answer(
        {"content": reviewed_answer, "references": sorted(set(references))},
        mode
    )

    return answer_dict
