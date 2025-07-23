from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
import unicodedata




def load_documents_from_pdf(directory_path):
    """ Return a list of documents extracted from PDF files in the specifed directory."""

    loader = DirectoryLoader(
        directory_path,
        glob="**/*.pdf",
        loader_cls=PyPDFLoader
    )

    documents = loader.load()

    return documents




def split_into_chunks(documents):
    """ Split the documents into smaller chunks for processing."""

    splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n","\n"],
        chunk_size = 200,
        chunk_overlap = 100
    )

    chunks = splitter.split_documents(documents)
    return chunks




def clean_metadata(metadata: dict) -> dict:
    clean_meta = {}
    for key, value in metadata.items():
        if isinstance(value, str):
            clean_meta[key] = value.encode("utf-8", "ignore").decode("utf-8").strip()
        else:
            clean_meta[key] = value
    return clean_meta




def clean_text(text):
    ''' Remove invalid unicode and control characters'''
    if not isinstance(text, str):
        return ""
    
    # Normalize and remove surrogates
    try:
        text = text.encode("utf-8", "replace").decode("utf-8")
    except:
        text = str(text)
    
    # Optionally remove control characters
    text = ''.join(ch for ch in text if unicodedata.category(ch)[0] != 'C' or ch in '\n\t ')
    
    return text.strip()




def load_embeddings():
    """ Load the embeddings model for vectorization."""

    embeddings=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

    return embeddings