import os
import re
import json
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

def analyze_code_with_llm(chunks):
    # Join the list of code chunks into a single string separated by newlines
    input_code = "\n\n".join(chunks)

    # Create a prompt template for analyzing the code
    prompt_template = PromptTemplate(
        input_variables=["code"],
        template="""  # Define the format for the prompt sent to the LLM
You are a code analysis assistant. Given the following Java code, extract and return structured information in JSON format. The JSON must contain:

- "project_overview": A short summary of what the project does.
- "key_methods": A list of key methods with their names, signatures, and what they do.
- "complexity_notes": Notes about code structure, testing, or design patterns used.

Return only the valid JSON, without markdown code blocks. Here's the code:

{code}
"""
    )

    # Initialize the LLM (Google's generative AI model) with the given settings
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",  # Specify the model to use
        temperature=0.2,  # Control randomness of the output
        google_api_key=os.getenv("GOOGLE_API_KEY")  # Use environment variable for API key
    )

    # Combine the prompt template and the LLM using the | operator (new style in LangChain)
    chain = prompt_template | llm

    # Use invoke method to generate a response from the LLM instead of the deprecated run method
    result = chain.invoke({"code": input_code})

    # Clean up the result by removing any unwanted markdown or JSON code block markers
    clean_text = re.sub(r"^```json\n?|```$", "", result.content.strip(), flags=re.MULTILINE)

    try:
        # Try to parse the cleaned text as JSON and return it
        return json.loads(clean_text)
    except json.JSONDecodeError:
        # If JSON parsing fails, print a warning and return the raw response
        print("⚠️ LLM response is not valid JSON. Saving raw string.")
        return {"raw_summary": clean_text}
