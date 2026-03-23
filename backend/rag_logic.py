import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
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
        
        # Modern LCEL-based RAG chain
        system_prompt = (
            "You are an assistant for question-answering tasks. "
            "Use the following pieces of retrieved context to answer "
            "the question. If you don't know the answer, say that you "
            "don't know. Use three sentences maximum and keep the "
            "answer concise."
            "\n\n"
            "{context}"
        )
        
        prompt = ChatPromptTemplate.from_messages(
            [
                ("system", system_prompt),
                ("human", "{input}"),
            ]
        )
        
        # Create the chains
        combine_docs_chain = create_stuff_documents_chain(self.llm, prompt)
        retrieval_chain = create_retrieval_chain(self.vector_db.as_retriever(), combine_docs_chain)
        
        # Using invoke as requested in the user prompt script
        response = retrieval_chain.invoke({"input": query})
        return response['answer']

rag_engine = RAGEngine()
