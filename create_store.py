from pinecone import Pinecone, ServerlessSpec,CloudProvider,VectorType,AwsRegion
from langchain_pinecone import PineconeVectorStore
from src.helpers import load_documents_from_pdf, split_into_chunks,clean_metadata,clean_text,load_embeddings
from langchain_core.documents import Document
from dotenv import load_dotenv
import os

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY


def create_pinecone_index(index_name):
    """ Create a Pinecone index for storing vector embeddings."""

    pc = Pinecone(api_key=PINECONE_API_KEY)


    if not pc.has_index(index_name):
        pc.create_index(
        name=index_name,
        dimension=384,
        spec=ServerlessSpec(
        cloud=CloudProvider.AWS,
        region=AwsRegion.US_EAST_1
        ),
        vector_type=VectorType.DENSE
        )
        print(f"Index {index_name} created successfully.")
    else:
        print(f"Index {index_name} already exists.")




if __name__ == "__main__":

    # Load documents from PDF files
    docs = load_documents_from_pdf("data/")

    # Split documents into chunks
    chunks = split_into_chunks(docs)

    # Clean metadata ant text
    cleaned_docs = []
    for doc in chunks:
        if isinstance(doc.page_content, str) and len(doc.page_content.strip()) > 10:
            cleaned_text = clean_text(doc.page_content)
            cleaned_meta = clean_metadata(doc.metadata)
            cleaned_docs.append(Document(page_content=cleaned_text, metadata=cleaned_meta))
    
    # Create Pinecone index
    index_name="aibot"
    create_pinecone_index(index_name)

    # Load embeddings
    embeddings= load_embeddings()

    # Create Pinecone vector store
    vectorstore = PineconeVectorStore.from_documents(
    documents=cleaned_docs,
    index_name=index_name,
    embedding=embeddings
    )