import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

load_dotenv()

class RAGEngine:
    def __init__(self):
        # Using bge-small-en-v1.5 as requested, runs locally
        self.embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-small-en-v1.5")
        self.vector_db = None
        # Groq LLM (Llama 3.3)
        self.llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0)

    def process_pdf(self, file_path):
        loader = PyPDFLoader(file_path)
        docs = loader.load()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        chunks = text_splitter.split_documents(docs)
        # Create FAISS vector store
        self.vector_db = FAISS.from_documents(chunks, self.embeddings)
        return len(chunks)

    def ask(self, query):
        if not self.vector_db:
            return "Please upload a PDF first."
        
        qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vector_db.as_retriever()
        )
        # Using invoke as requested in the user prompt script
        response = qa_chain.invoke(query)
        return response['result']

rag_engine = RAGEngine()
