import os
import re
import json
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Analyze a list of code chunks using an LLM and return structured JSON output
def analyze_code_with_llm(chunks):
    input_code = "\n\n".join(chunks)
    prompt_template = PromptTemplate(
        input_variables=["code"],
        template="""You are a code analysis assistant. Given the following Java code, extract and return structured information in JSON format. The JSON must contain:
- "project_overview": A short summary of what the project does.
- "key_methods": A list of key methods with their names, signatures, and what they do.
- "complexity_notes": Notes about code structure, testing, or design patterns used.
Return only the valid JSON, without markdown code blocks. Here's the code:
{code}
"""
    )
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
        temperature=0.2,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )
    chain = prompt_template | llm
    result = chain.invoke({"code": input_code})
    clean_text = re.sub(r"^```json\n?|```$", "", result.content.strip(), flags=re.MULTILINE)
    try:
        return json.loads(clean_text)
    except json.JSONDecodeError:
        print("⚠️ LLM response is not valid JSON. Saving raw string.")
        return {"raw_summary": clean_text}
