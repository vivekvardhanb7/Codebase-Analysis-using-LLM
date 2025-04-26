import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

def build_vector_store(chunks):
    # Loading the pre-trained model to convert code chunks into embeddings
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # Converting the chunks into embeddings using the model
    embeddings = model.encode(chunks)

    # Get the dimension (length) of the embedding vectors
    dim = embeddings[0].shape[0]
    
    # Creating a FAISS index for storing embeddings and performing similarity searches
    index = faiss.IndexFlatL2(dim)
    
    # Add the embeddings to the FAISS index for searching
    index.add(np.array(embeddings))

    return index, embeddings  # Return the index and embeddings

def query_faiss(index, chunks, query_text):
    # Loading the pre-trained model to convert the query into an embedding
    model = SentenceTransformer('all-MiniLM-L6-v2')
    
    # Converting the query into an embedding using the model
    query_vec = model.encode([query_text])
    
    # Perform a search in the FAISS index to find the most similar code chunks
    D, I = index.search(np.array(query_vec), k=5)  # Get top 5 similar chunks
    
    # Return the top 5 code chunks that are most similar to the query
    return [chunks[i] for i in I[0]]
