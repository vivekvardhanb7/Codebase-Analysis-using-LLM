import streamlit as st
import os
from clone_repo import clone_repo
from load_split import load_code_files, split_code
from buildvector_faiss import build_vector_store, query_faiss
from analyze_code import analyze_code_with_llm
from save_output import save_output

st.set_page_config(page_title="Code Analyzer tool using LLM", layout="wide")

st.title("📊Code Analyzer tool using LLM")


repo_url = st.text_input("🔗 Enter GitHub repository URL:", "https://github.com/janjakovacevic/SakilaProject")
local_folder = repo_url.split('/')[-1]

if st.button("📥 Clone Repository"):
    clone_repo(repo_url, local_folder)
    st.success(f"Repository cloned to `{local_folder}/`")


if os.path.exists(local_folder):
    st.write("✅ Repository found. Loading Java files...")
    code_files = load_code_files(local_folder)
    all_chunks = []
    for _, code in code_files:
        all_chunks.extend(split_code(code))
    st.write(f"🔍 Loaded and split **{len(code_files)}** Java files into **{len(all_chunks)}** chunks.")

    
    index, _ = build_vector_store(all_chunks)

    
    user_query = st.text_input("❓ What would you like to know about the project?", "Give me an overview and key methods.")

    if st.button("🔎 Analyze Code"):
        top_chunks = query_faiss(index, all_chunks, user_query)
        structured_summary = analyze_code_with_llm(top_chunks)

        
        save_output(structured_summary)

        
        st.subheader("📋 Analysis Result")
        st.json(structured_summary)
        st.success("✅ Analysis complete and saved to `output.json`")
else:
    st.warning("⚠️ Please clone a repository first.")

