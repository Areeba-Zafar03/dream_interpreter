# dream_bot.py

import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI

# Set your Gemini API key
os.environ["GOOGLE_API_KEY"] = "AIzaSyAcQsVzPNzfFYFrmMJrBK5MG8MZwjz20uM"  # Replace with your key

def build_or_load_vectorstore():
    index_path = "dream_faiss_index"
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    if not os.path.exists(index_path):
        print("📘 Loading Ibn Sirin book...")
        loader = PyPDFLoader("ibn_sirin_book.pdf")
        pages = loader.load()

        print("✂️ Splitting pages into chunks...")
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        docs = splitter.split_documents(pages)

        print("🧠 Generating embeddings and saving index...")
        vectorstore = FAISS.from_documents(docs, embedding_model)
        vectorstore.save_local(index_path)
        print("✅ Embeddings created and index saved.")
    else:
        print("🔄 Loading existing FAISS index...")

    return FAISS.load_local(index_path, embedding_model, allow_dangerous_deserialization=True)

def get_qa_chain():
    vectorstore = build_or_load_vectorstore()
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.3)
    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=vectorstore.as_retriever(search_type="similarity", k=4),
        return_source_documents=False
    )
    return qa
