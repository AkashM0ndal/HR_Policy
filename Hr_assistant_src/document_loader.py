""" Step 1: Read the raw document from the data folder."""

from langchain_community.document_loaders import TextLoader
from Hr_assistant_src import config


def load_document(file_path: str= config.DATA_FILE_PATH):
    """Load a .txt file adn return it as a list of Langchain Document"""
    loader= TextLoader(file_path, autodetect_encoding= True)
    return loader.load()