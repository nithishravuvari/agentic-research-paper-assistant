import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

DB_DIR = "data/chroma_db"

def build_rag_pipeline():
    """Build and return a Retrieval-QA chain."""
    embedding = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    db = Chroma(persist_directory=DB_DIR, embedding_function=embedding)
    retriever = db.as_retriever(search_kwargs={"k": 3})
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0, api_key=OPENAI_API_KEY)

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )
    return qa_chain

def retrieve_docs(query: str, k: int = 3):
    embedding = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    db = Chroma(persist_directory=DB_DIR, embedding_function=embedding)
    retriever = db.as_retriever(search_kwargs={"k": k})
    return retriever.invoke(query)  # modern API


def run_query(query: str):
    """Run a single query through the RAG pipeline and return structured result."""
    qa = build_rag_pipeline()
    response = qa.invoke(query)

    # Format nicely
    result = {
        "answer": response["result"],
        "sources": [
            {
                "title": doc.metadata.get("title", "N/A"),
                "authors": doc.metadata.get("authors", "N/A"),
            }
            for doc in response["source_documents"]
        ],
    }
    return result

# (Optional) Allow standalone testing
if __name__ == "__main__":
    query = "How are generative models used for turbulent flows?"
    result = run_query(query)

    print("\n=== Answer ===")
    print(result["answer"])

    print("\n=== Sources ===")
    for src in result["sources"]:
        print(f"- {src['title']} | Authors: {src['authors']}")
