# Agentic Research Paper Assistant 📑🤖  

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)  
![LangChain](https://img.shields.io/badge/LangChain-Agentic-yellow?style=for-the-badge)  
![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector%20Store-orange?style=for-the-badge)  
![OpenAI](https://img.shields.io/badge/OpenAI-API-blueviolet?style=for-the-badge)  
![Rich](https://img.shields.io/badge/rich-terminal%20printing-purple?style=for-the-badge)

An **Agentic RAG (Retrieval-Augmented Generation) pipeline** that acts as a **Research paper Assistant**.  
It ingests research papers, preprocesses them, retrieves relevant context, and generates **detailed answers, concise summaries, and structured comparisons** — powered by embeddings, retrieval, and agent-like planning/criticism steps.  

---

## ✨ Features  

- **Paper ingestion & preprocessing** (JSON, PDFs → embeddings via ChromaDB).  
- **Agentic RAG pipeline** with planner, retriever, summarizer, and critic agents.  
- **Multiple answer formats**:  
  - 📄 **Detailed Answer** (long-form structured output)  
  - 📝 **Concise Summary** (shorter structured overview)  
  - 📊 **Comparison Result** (side-by-side challenge vs. advances)  
- **Pretty printer** for formatting final outputs (`--rich` flag).  
- **Extensible architecture** for future agents (bias detection, citation linking, etc.).  

---

## 1. Table of Contents  

1. [Dataset / Papers](#2-dataset--papers)  
2. [Libraries Used](#3-libraries-used)  
3. [How to Install and Run the Project](#4-how-to-install-and-run-the-project)  
4. [How to Use the Project](#5-how-to-use-the-project)  
5. [Results](#6-results) 

---

## 2. Dataset / Papers

- Example input papers are stored in:
  ```bash
  data/papers.json

- Vectorized into embeddings and stored in:
  ```bash
  data/chroma_db/

---

## 3. Libraries Used  

- **langchain** → Agent orchestration and RAG pipeline.  
- **chromadb** → Vector database for semantic search.  
- **openai** → LLM-powered text generation.  
- **tiktoken** → Token counting and handling.  
- **pydantic** → Data validation and structured output.  
- **rich** → Pretty terminal printing for better readability.  

---

---
## 4. How to Install and Run the Project

1.  **Clone the repository:**
    ```bash
     git clone https://github.com/nithishravuvari/agentic-research-paper-assistant.git
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd agentic-research-paper-assistant
    ```
3.  **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python -m venv envi_rag
    ```
    ```bash
    source envi_rag/bin/activate   # Mac/Linux
    ```
    ```bash
    envi_rag\Scripts\activate      # Windows
    ```
4.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
5.  **Run the pipeline with different modes:**
    ```bash
    # Generate a detailed structured answer
    python main.py --mode detailed --rich  

    # Generate a concise structured summary
    python main.py --mode concise --rich  

    # Generate a comparison (Challenges vs Advances)
    python main.py --mode comparison --rich  
    ```

---
## 5. How to Use the Project

-   **Place your research papers** (PDF/JSON) in the `data/` folder.
-   **Choose the output mode** using `--mode`:
    -   `detailed` → Long structured answer.
    -   `concise` → Shorter summary.
    -   `comparison` → Challenges vs Advances comparison.
-   **Add `--rich`** to enable pretty-printed formatting in the terminal.
-   Outputs are displayed in the console and can be extended to UI/API.

---
## 6. Results

Here are example outputs from the pipeline:

**🔹 Detailed Answer**
    <img width="955" height="825" alt="image" src="https://github.com/user-attachments/assets/013cdc28-94a0-439e-bbfa-8fc8c16cf0eb" />

**🔹 Concise Summary**
    ![Concise Summary](https://github.com/user-attachments/assets/689c4036-3339-43f7-b44c-d3f448123f17)

**🔹 Comparison Result**
    ![Comparison Result](https://github.com/user-attachments/assets/1b03b9b5-cd63-4075-beca-50bfac005e35)
