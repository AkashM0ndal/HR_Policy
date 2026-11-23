# HR Policy RAG Assistant 🤖

## 📌 Project Overview

The **HR Policy RAG Assistant** is a Retrieval-Augmented Generation (RAG) project built using Python, LangChain, FAISS, Jina Embeddings, and Groq LLM.

This project allows users to ask questions about HR policies and receive relevant answers based on the provided HR policy document.

Instead of relying only on the LLM's internal knowledge, the system retrieves relevant information from the document and uses it as context to generate accurate, document-based responses.

## 🚀 Features

- Load and process HR policy documents.
- Split large documents into smaller text chunks.
- Generate vector embeddings using Jina Embeddings.
- Store document embeddings in a FAISS vector database.
- Perform semantic similarity search.
- Retrieve the top 3 relevant document chunks.
- Generate answers using Groq LLM.
- Use a LangChain AI Agent with a custom HR policy retrieval tool.
- Avoid guessing when information is not available in the retrieved context.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| LangChain | RAG pipeline and AI Agent |
| Jina Embeddings | Text embedding generation |
| FAISS | Vector database |
| Groq | LLM inference |
| python-dotenv | Environment variable management |
| Jupyter Notebook | Development and experimentation |

## 📂 Project Structure

```text
HR-Policy-RAG/
│
├── Data/
│   └── Policy.txt
│
├── Data_ingesation.ipynb
│
├── .env
│
├── requirements.txt
│
├── .gitignore
│
└── README.md
```

## ⚙️ How It Works

The project follows a standard RAG architecture.

### 1. Data Ingestion
- Load the HR policy document using LangChain's `TextLoader`.
- Extract the document content and metadata.

### 2. Text Splitting
- Split the document into smaller chunks using `RecursiveCharacterTextSplitter`.
- Chunk Size: 300
- Chunk Overlap: 80

### 3. Embedding Generation
- Convert text chunks into numerical vector representations.
- Use the `jina-embeddings-v2-base-en` embedding model.

### 4. Vector Database
- Store the generated embeddings in a FAISS vector database.
- Enable efficient similarity-based retrieval.

### 5. Data Retrieval
- Convert the user's question into an embedding.
- Search for semantically relevant document chunks.
- Retrieve the top 3 matching chunks.

### 6. LLM Integration
- Use Groq's `openai/gpt-oss-20b` model.
- Provide retrieved document content to the LLM for generating answers.

### 7. AI Agent
- Create an AI Agent using LangChain's `create_agent`.
- Integrate the custom `search_hr_policy` retrieval tool.
- Instruct the agent to retrieve information before answering.
- Return an appropriate response when information is unavailable.

## 🔄 RAG Architecture

```text
              HR Policy Document
                      |
                      v
                 Text Loader
                      |
                      v
                Text Splitting
                      |
                      v
                Jina Embeddings
                      |
                      v
                 FAISS Vector DB
                      |
                      |
              User Question
                      |
                      v
               Query Embedding
                      |
                      v
               Similarity Search
                      |
                      v
              Retrieve Top 3 Chunks
                      |
                      v
                   Groq LLM
                      |
                      v
                 LangChain Agent
                      |
                      v
                Final Answer
```

## 📥 Installation and Setup

### 1. Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

### 2. Navigate to the Project Directory

```bash
cd HR-Policy-RAG
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment.

**Windows:**

```bash
.venv\Scripts\activate
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install langchain langchain-community langchain-text-splitters langchain-groq faiss-cpu python-dotenv jupyter
```

## 🔑 Environment Variables

Create a `.env` file in the root directory.

Add your API keys:

```env
GROQ_API_KEY=your_groq_api_key
JINA_API_KEY=your_jina_api_key
```

Get your API keys from:

- **Groq:** https://console.groq.com/
- **Jina AI:** https://jina.ai/

**Important:** Never upload your `.env` file or expose your API keys on GitHub.

## ▶️ Run the Project

### 1. Start Jupyter Notebook

```bash
jupyter notebook
```

### 2. Open the Notebook

Open:

```text
Data_ingesation.ipynb
```

### 3. Configure the Document Path

Make sure the document path in the `TextLoader` section points to your HR policy file.

Example:

```python
loader = TextLoader(
    "Data/Policy.txt",
    autodetect_encoding=True
)
```

### 4. Execute All Cells

Run the notebook cells in order to:

- Load the document.
- Split the text.
- Generate embeddings.
- Create the FAISS vector database.
- Initialize the retriever.
- Configure the Groq LLM.
- Create the HR Assistant Agent.

### 5. Ask Questions

Once the notebook has initialized the agent, use the following function:

```python
ask_hr_assistant("What is the company's leave policy?")
```

## 💬 Example Questions

You can ask questions related to:

- What is the company's leave policy?
- How many days can employees work from home?
- What is the probation period?
- What is the employee notice period?
- What is the reimbursement policy?
- What are the rules regarding holidays?
- What is the company's exit policy?
- What is the code of conduct?

## ⚙️ Model Configuration

| Component | Configuration |
|---|---|
| Embedding Model | jina-embeddings-v2-base-en |
| Vector Database | FAISS |
| Text Splitter | RecursiveCharacterTextSplitter |
| Chunk Size | 300 |
| Chunk Overlap | 80 |
| Retrieval Count (K) | 3 |
| LLM Provider | Groq |
| LLM Model | openai/gpt-oss-20b |
| Temperature | 0.7 |
| AI Agent Framework | LangChain |

## 🎯 Learning Objectives

This project demonstrates practical implementation of:

- Understanding Retrieval-Augmented Generation (RAG).
- Document loading and preprocessing.
- Text chunking strategies.
- Semantic search and vector embeddings.
- Vector database implementation using FAISS.
- Integrating LLMs with external documents.
- Building custom retrieval tools.
- Creating AI Agents using LangChain.

## 🔮 Future Improvements

- Support PDF, DOCX, and multiple document formats.
- Build a user interface using Streamlit.
- Develop REST APIs using FastAPI.
- Add conversational memory.
- Support multiple knowledge sources.
- Implement advanced retrieval and reranking.
- Add document upload functionality.

## 👨‍💻 Author

- Name: Akash Mondal
- email: skyakash.ml@gmail.com
- Contact No.: +91 9083666706

Developed as a hands-on project to understand and implement Retrieval-Augmented Generation, LangChain, vector databases, embeddings, and AI Agents.

---
⭐ If you find this project useful, consider giving it a star!