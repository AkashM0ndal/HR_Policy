""" Step 3: Turn text into numbers (vectors) using Jina."""

from langchain_community.embeddings import JinaEmbeddings
from Hr_assistant_src import config


def get_embedding_model():
    """Return a Jina embeddings model.
    Reads JINA_API_KEY from the environment."""

    return JinaEmbeddings(model_name= config.EMBEDDING_MODEL_NAME, jina_api_key= config.JINA_API_KEY)




