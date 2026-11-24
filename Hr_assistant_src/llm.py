"""Step 6: Connect to the LLM (the 'brain' of the assistant)"""

from langchain_groq import ChatGroq
from Hr_assistant_src import config

def get_llm():
    """Return a Groq chat model. Reads GROQ_API_KEY from the environment."""
    return ChatGroq(model= config.LLM_MODEL_NAME, temperature= config.LLM_TEMPERATURE)