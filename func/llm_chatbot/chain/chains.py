from pathlib import Path
from typing import Union

from langchain_community.llms.ollama import Ollama


def create_conversational_retrieval_chain(model: Union[str, Path]):
    if isinstance(model, str):
        llm = Ollama(model=model)

