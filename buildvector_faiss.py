import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

# Build a FAISS vector store from a list of text/code chunks
def build_vector_store(chunks):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(chunks)
    dim = embeddings[0].shape[0]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    return index, embeddings

# Query the FAISS index to retrieve top 5 similar chunks for a given query text
def query_faiss(index, chunks, query_text):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    query_vec = model.encode([query_text])
    D, I = index.search(np.array(query_vec), k=5)
    return [chunks[i] for i in I[0]]
