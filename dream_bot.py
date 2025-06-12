#dream_bot.py

import os
import json
import traceback
from datetime import datetime
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

# Set Groq API Key
os.environ["OPENAI_API_KEY"] = "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"  # Replace with your actual key

# Book paths
BOOKS = {
    "ibn_sirin": "ibn_sirin_book.pdf",
    "ibn_raashid": "ibn_raashid_book.pdf"
}

HISTORY_FILE = "dream_history.json"

def load_dream_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_dream_to_history(dream, interpretations):
    history = load_dream_history()
    entry = {
        "timestamp": datetime.now().isoformat(),
        "dream": dream,
        "interpretations": interpretations
    }
    history.append(entry)
    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)

def get_multi_book_qa_results(query):
    try:
        # Use CPU to avoid meta tensor GPU issues
        embedding_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2",
            model_kwargs={"device": "cpu"}
        )
    except Exception as e:
        print("Embedding model loading failed:", e)
        traceback.print_exc()
        raise

    results = {}
    for book_key, book_path in BOOKS.items():
        index_path = f"dream_faiss_index_{book_key}"
        try:
            if not os.path.exists(index_path):
                loader = PyPDFLoader(book_path)
                pages = loader.load()
                splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
                docs = splitter.split_documents(pages)
                vectorstore = FAISS.from_documents(docs, embedding_model)
                vectorstore.save_local(index_path)
            else:
                vectorstore = FAISS.load_local(index_path, embedding_model, allow_dangerous_deserialization=True)

            llm = ChatOpenAI(
                model="llama3-70b-8192",
                base_url="https://api.groq.com/openai/v1",
                temperature=0.7,
                max_tokens=600
            )

            qa = RetrievalQA.from_chain_type(
                llm=llm,
                retriever=vectorstore.as_retriever(search_type="similarity", k=4),
                return_source_documents=False
            )

            short_prompt = f"""Interpret the following dream using insights from the book '{book_key.replace('_', ' ').title()}'. 
Respond clearly in 10 to 15 short lines.

Dream: {query}"""
            interpretation = qa.run(short_prompt)
            results[book_key] = interpretation.strip()

        except Exception as e:
            results[book_key] = f"Error processing {book_key}: {e}"
            print(f"[ERROR] {book_key}: {e}")
            traceback.print_exc()

    # Save to history
    save_dream_to_history(query, results)
    return results
