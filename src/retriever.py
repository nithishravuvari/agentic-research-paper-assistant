import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

DB_DIR = "data/chroma_db"

# Load embedding function
embedding = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)

# Reload Chroma DB with embeddings
db = Chroma(persist_directory=DB_DIR, embedding_function=embedding)

# Create retriever
retriever = db.as_retriever(search_kwargs={"k": 3})

# Example query
query = "What are recent advances in GNNs?"
results = retriever.invoke(query)  # new .invoke API replaces .get_relevant_documents

for i, doc in enumerate(results, 1):
    print(f"\nResult {i}:")
    print("Title:", doc.metadata.get("title", "N/A"))
    print("Authors:", doc.metadata.get("authors", "N/A"))
    print("Content:", doc.page_content[:200], "...")