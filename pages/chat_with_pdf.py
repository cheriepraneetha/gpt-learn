 # Replace with your Jina API key
  # Replace with your Groq API key

import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import HuggingFaceEmbeddings  # ✅ Free, Local Embeddings
from langchain.vectorstores import FAISS
from langchain_groq import ChatGroq  # ✅ Correct import
import tempfile
import os

# ✅ Groq API Key (Replace with your actual key)
GROQ_API_KEY = "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" # ⚠️ Don't expose this key publicly!

# ✅ Configure LLM (Groq API)
llm = ChatGroq(model_name="llama3-70b-8192", api_key=GROQ_API_KEY)

# ✅ Streamlit UI
st.title("📄 Chat with your PDF")

# ✅ Upload PDF
pdf = st.file_uploader("Upload your PDF", type=["pdf"])
if pdf:
    # 🔹 Save the uploaded file to a temporary location
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
        tmp_file.write(pdf.read())
        pdf_path = tmp_file.name  # Get the temporary file path

    # ✅ Load and process PDF
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    # ✅ Convert docs to text (needed for FAISS)
    text_docs = [doc.page_content for doc in docs]

    # ✅ Embed documents using Hugging Face (Completely Free)
    embedder = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # ✅ Create FAISS Vector Store
    vectorstore = FAISS.from_texts(text_docs, embedder)

    st.success("✅ PDF Processed!")

    # ✅ Chat Interface
    query = st.text_input("Ask a question from the PDF:")
    if query:
        retrieved_docs = vectorstore.similarity_search(query, k=3)

        # ✅ Extract and format text content properly
        context = "\n\n".join([doc.page_content for doc in retrieved_docs])  

        # ✅ Pass to LLM
        response = llm.invoke(f"Context:\n{context}\n\nQuestion: {query}")

        st.write("🧠 Answer:", response.content) 

    # ✅ Cleanup: Remove temp file after processing
    os.remove(pdf_path)
