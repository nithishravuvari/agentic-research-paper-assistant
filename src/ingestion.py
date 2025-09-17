import arxiv
import os
import json

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

def fetch_papers(query="graph neural networks", max_results=20):
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )
    papers = []
    for result in search.results():
        paper_data = {
            "title": result.title,
            "summary": result.summary,
            "authors": [a.name for a in result.authors],
            "pdf_url": result.pdf_url
        }
        papers.append(paper_data)

    with open(os.path.join(DATA_DIR, "papers.json"), "w", encoding="utf-8") as f:
        json.dump(papers, f, indent=2)

    print(f"Saved {len(papers)} papers to data/papers.json")

if __name__ == "__main__":
    fetch_papers()