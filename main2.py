# Importing necessary modules
from clone_repo import clone_repo
from load_split import load_code_files, split_code
from buildvector_faiss import build_vector_store, query_faiss
from analyze_code import analyze_code_with_llm
from save_output import save_output
import os

if __name__ == "__main__":
    # Clone the Sakila repo if not already cloned
    if not os.path.exists("sakila"):
        clone_repo("https://github.com/janjakovacevic/SakilaProject", "sakila")

    # Load code files from the cloned repo
    code_files = load_code_files("sakila/")

    # Split code into smaller chunks
    all_chunks = []
    for _, code in code_files:
        all_chunks.extend(split_code(code))

    # Build a FAISS vector store from the code chunks
    index, _ = build_vector_store(all_chunks)

    while True:
        user_query = input("What would you like to know about the SakilaProject? (type 'exit' to quit): ")
        if user_query.lower() == 'exit':
            break

        # Query FAISS to get top code chunks
        top_chunks = query_faiss(index, all_chunks, user_query)

        # Analyze the top chunks using LLM
        structured_summary = analyze_code_with_llm(top_chunks)

        # Save the structured analysis to a JSON output file
        save_output(structured_summary)

    # Additionally, analyze controller files individually for richer detail
    controller_files = [
        f for f in code_files if "controller" in f[0].lower()
    ]

    for filename, code in controller_files:
        controller_chunks = split_code(code)
        controller_output = analyze_code_with_llm(controller_chunks)
        base_filename = os.path.basename(filename).replace(".java", "_analysis.json")
        save_output(controller_output, output_path=f"output/controllers/{base_filename}")
