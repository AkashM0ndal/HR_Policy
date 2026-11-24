""" All settings for teh app live here, in one place"""

import os 
from dotenv import load_dotenv

load_dotenv()

## ENV VAR / SECRET

GROQ_API_KEY= os.getenv('GROQ_API_KEY')
JINA_API_KEY= os.getenv('JINA_API_KEY')


## Define Path - DATA / VECTOR STORE

DATA_FILE_PATH= os.path.join('Data', 'Policy.txt')

# Vector Store path

VECTOR_STORE_PATH= os.path.join('Data', 'faiss_index')


## Models
# LLM and EMBEDDING MODEL

LLM_MODEL_NAME= 'openai/gpt-oss-20b'
LLM_TEMPERATURE= 0.4

EMBEDDING_MODEL_NAME= 'jina-embeddings-v2-base-en'


# CHUNK / TEXT SPLITTING CONFIG

CHUNK_SIZE= 500
CHUNK_OVERLAP= 60


# Retrieveal Results
TOP_K_RESULTS= 3

## System_Instructions

SYSTEM_PROMPT= (
    """your are a friendly HR assistant.
        My org name is Sky Company Pvt Ltd.
        Always use the search_hr_policy tool to look up
        facts before answering
        If the answer isn't in the search results, say you don't know " 
        Instead of guessing.
    """
)


def check_api_keys() -> None:
    """Stop early with a clear message if a required API key is misssing."""
    if not GROQ_API_KEY:
        raise ValueError('Missing GROQ_API_KEY. Please add it to your .env file.')

    if not JINA_API_KEY:
        raise ValueError('Missing JINA_API_KEY. Please add it to your .env file.')


