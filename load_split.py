import os
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Reading all Java files from the directory which the files ends with .java
def load_code_files(directory):
    code_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".java"):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    code = f.read()
                    code_files.append((path, code))
    return code_files


# Spliting code into chunks to handle token limits
def split_code(code):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return splitter.split_text(code)