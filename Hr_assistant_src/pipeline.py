"""Wires all teh components together into one ready-to-use agent.

This is the single entry point that main.py (CLI) and app.py (Streamlit)
both call. Each step is handeled by its own small module."""



from Hr_assistant_src import config 
from Hr_assistant_src.agent import create_hr_agent
from Hr_assistant_src.document_loader import load_document
from Hr_assistant_src.llm import get_llm 
from Hr_assistant_src.splitter import split_into_chunks
from Hr_assistant_src.tools import create_search_tool
from Hr_assistant_src.vector_store import (
    build_vector_store,
    get_retriever,
    load_vector_store,
    save_vector_store,
    vector_store_exists,
)


def build_vector_store_for_documents(file_path: str= config.DATA_FILE_PATH):
    """Load + split + embed the document, reusing a saved index if we have one."""
    if vector_store_exists():
        print('Found a saved vector store on disk, loading it (fast, no re-embeddings)')
        return load_vector_store()

    print('No saved vector store found, building one from scratch...')
    documents= load_document(file_path)
    chunks= split_into_chunks(documents)
    print(f'Loaded "{file_path}" and split it into {len(chunks)} chunks.')


    vector_store= build_vector_store(chunks)
    save_vector_store(vector_store)
    print('Vector Store built and saved to disk for next time.')
    return vector_store



def build_hr_assistant(file_path: str= config.DATA_FILE_PATH):
    """Build the full RAG agent, ready to answer questions."""

    config.check_api_keys()

    vector_store = build_vector_store_for_documents(file_path)
    retriever = get_retriever(vector_store)
    search_tool = create_search_tool(retriever)

    llm = get_llm()
    agent = create_hr_agent(llm, [search_tool])

    return agent



def ask(agent, question: str) -> str:
    """Ask the final question and return its final answer as plain text."""

    response= agent.invoke({'messages': [{'role': 'user', 'content': question}]})
    return response['messages'][-1].content






