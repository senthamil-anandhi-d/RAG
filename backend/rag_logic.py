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
        print(f"DEBUG: Processing PDF at {file_path}")
        loader = PyPDFLoader(file_path)
        docs = loader.load()
        print(f"DEBUG: PDF loaded. {len(docs)} pages found.")
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        chunks = text_splitter.split_documents(docs)
        print(f"DEBUG: Text split into {len(chunks)} chunks.")
        # Create FAISS vector store
        print("DEBUG: Creating FAISS index...")
        self.vector_db = FAISS.from_documents(chunks, self.embeddings)
        print("DEBUG: FAISS index created successfully.")
        return len(chunks)

    def ask(self, query):
        print(f"DEBUG: Internal ask method called with query: {query}")
        if not self.vector_db:
            print("DEBUG: No vector database found. User needs to upload PDF.")
            return "Please upload a PDF first."
        
        try:
            # Modern LCEL-based RAG chain
            print("DEBUG: Setting up system prompt...")
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
            
            print("DEBUG: Initializing combine_docs_chain...")
            combine_docs_chain = create_stuff_documents_chain(self.llm, prompt)
            
            print("DEBUG: Initializing retrieval_chain...")
            retrieval_chain = create_retrieval_chain(self.vector_db.as_retriever(), combine_docs_chain)
            
            print("DEBUG: Invoking chain...")
            response = retrieval_chain.invoke({"input": query})
            print("DEBUG: Chain invocation successful.")
            return response['answer']
        except Exception as e:
            print(f"DEBUG: Exception in rag_engine.ask: {str(e)}")
            import traceback
            traceback.print_exc()
            raise e

rag_engine = RAGEngine()
