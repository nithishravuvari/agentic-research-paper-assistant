import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from preprocessing import chunk_papers

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

DB_DIR = "data/chroma_db"

def build_vector_db():
    chunks = chunk_papers()
    texts = [c["chunk"] for c in chunks]
    # convert authors list → comma separated string
    metadatas = [{"title": c["title"], "authors": ", ".join(c["authors"])} for c in chunks]

    embedding = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    db = Chroma.from_texts(texts, embedding, metadatas=metadatas, persist_directory=DB_DIR)
    # db.persist()
    print("Vector DB built and persisted!")

if __name__ == "__main__":
    build_vector_db()
