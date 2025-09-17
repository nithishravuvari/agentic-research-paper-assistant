import json
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter

DATA_DIR = "data"

def load_papers():
    with open(os.path.join(DATA_DIR, "papers.json"), "r", encoding="utf-8") as f:
        return json.load(f)

def chunk_papers(chunk_size=1000, overlap=200):
    papers = load_papers()
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=overlap)

    chunks = []
    for paper in papers:
        text = paper["summary"]  # For MVP we use abstracts
        splits = splitter.split_text(text)
        for chunk in splits:
            chunks.append({
                "title": paper["title"],
                "authors": paper["authors"],
                "chunk": chunk
            })
    return chunks

if __name__ == "__main__":
    chunks = chunk_papers()
    print(f"Created {len(chunks)} text chunks from papers.")
