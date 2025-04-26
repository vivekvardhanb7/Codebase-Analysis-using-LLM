# Codebase-Analysis-using-LLM

This project provides an automatic code analysis for Java-based repositories. It performs the following key tasks:

1. **Clone a GitHub repository**  
   - If the repository is not already cloned, it will clone the repository into a specified directory.

2. **Read and split Java code**  
   - Loads Java files from the repository and splits them into smaller chunks to handle token limits.

3. **Build a vector store**  
   - Uses FAISS (Facebook AI Similarity Search) to build a vector store from the code chunks for efficient semantic search.

4. **Query the vector store**  
   - Accepts a user query to search the vector store and retrieves the most relevant code chunks.

5. **Analyze code with LLM**  
   - Sends the top-matching code chunks to Google's Generative AI model and extracts structured information in JSON format.

6. **Save the output**  
   - Saves the structured summary into a `JSON` file.

---

## Setup Instructions

### 1. Clone the repository

First, clone this project to your local machine:

```bash
git clone https://github.com/your-repository/Code-Analysis-Project.git
cd Code-Analysis-Project
```

---

### 2. Install Dependencies

Ensure you have **Python 3.8** or higher installed.  
Then install the required dependencies:

```bash
pip install -r requirements.txt
```

**Dependencies include**:
- `langchain`
- `langchain-google-genai`
- `sentence-transformers`
- `faiss-cpu`
- `python-dotenv`
- `numpy`

---

### 3. Set Up Environment Variables

You will need a Google API key to access Gemini models.  

Create a `.env` file in the root directory and add:

```env
GOOGLE_API_KEY=your_google_api_key
```

Replace `your_google_api_key` with your actual API key.

---

### 4. Run the Project

Run the following command:

```bash
python main.py
```

This will perform the following:
- Clone the Sakila repository (if not already cloned).
- Load and split Java files.
- Build the FAISS vector store.
- Accept a user query.
- Analyze the matching code using Gemini LLM.
- Save the output to a JSON file.

---

## Example Query

When you run the project, you will see:

```bash
What would you like to know about the SakilaProject?
```

Example queries you can ask:
- "What are the key classes in the SakilaProject?"
- "What does the method getCustomer do?"
- "Explain the database connection part."

---

## Project Structure

| File Name             | Purpose                                                                 |
|------------------------|------------------------------------------------------------------------|
| `clone_repo.py`         | Contains the function to clone a GitHub repository.                   |
| `load_split.py`         | Loads Java files and splits code into manageable chunks.              |
| `buildvector_faiss.py`  | Builds the FAISS vector store and handles semantic search operations. |
| `analyze_code.py`       | Sends code to LLM and processes the analysis response.                |
| `save_output.py`        | Saves the final JSON output.                                          |
| `main.py`               | Main entry point integrating all functionalities.                    |

---

## License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for details.

---



