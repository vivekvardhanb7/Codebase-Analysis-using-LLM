# Importing necessary modules
from clone_repo import clone_repo
from load_split import load_code_files
from load_split import split_code
from buildvector_faiss import build_vector_store
from buildvector_faiss import query_faiss
from analyze_code import analyze_code_with_llm
from save_output import save_output

 # End-to-end pipeline to clone, process, analyze, and save codebase insights
if __name__ == "__main__":
    clone_repo("https://github.com/janjakovacevic/SakilaProject", "sakila")  
    
    code_files = load_code_files("sakila/") 

    all_chunks = []  
    for _, code in code_files:
        all_chunks.extend(split_code(code))  

    index, _ = build_vector_store(all_chunks) 

    user_query = input("What would you like to know about the SakilaProject? ") 

    top_chunks = query_faiss(index, all_chunks, user_query) 

    structured_summary = analyze_code_with_llm(top_chunks)  

    save_output(structured_summary)  # Save the structured analysis to an output file
