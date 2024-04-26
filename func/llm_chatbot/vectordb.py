import shutil
from pathlib import Path
from typing import Union

from langchain_community.document_loaders.markdown import UnstructuredMarkdownLoader
from langchain_community.document_loaders.pdf import UnstructuredPDFLoader
from langchain_community.document_loaders.unstructured import UnstructuredFileLoader
from langchain_community.document_loaders.word_document import UnstructuredWordDocumentLoader
from langchain_community.embeddings.huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores.chroma import Chroma
from langchain_core.vectorstores import VectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter
from tqdm import tqdm

from settings import PERSISTENT_DIRECTORY, LOCAL_EMBEDDINGS, KG_DATA_PATH, KG_PROCESSED_DATA_PATH


def create_vectordb(model: Union[str, Path]) -> VectorStore:
    if model in LOCAL_EMBEDDINGS:
        model = str(LOCAL_EMBEDDINGS[model])
    embeddings = HuggingFaceEmbeddings(model_name=model)
    vectordb = Chroma(persist_directory=str(PERSISTENT_DIRECTORY), embedding_function=embeddings)
    return vectordb


def reload_vectordb(model: Union[str, Path]) -> None:
    if model in LOCAL_EMBEDDINGS:
        model = str(LOCAL_EMBEDDINGS[model])
    files = []
    for suffix in ["md", "txt", "docx", 'pdf']:
        for fpath in KG_DATA_PATH.glob(f"**/*.{suffix}"):
            files.append(str(fpath))
    docs = []
    import pdb; pdb.set_trace()
    if len(docs) == 0:
        return
    for one_file in tqdm(files):
        file_type = one_file.split('.')[-1]
        if file_type == 'md':
            loader = UnstructuredMarkdownLoader(one_file)
        elif file_type == 'txt':
            loader = UnstructuredFileLoader(one_file)
        elif file_type == 'docx':
            loader = UnstructuredWordDocumentLoader(one_file)
        elif file_type == 'pdf':
            loader = UnstructuredPDFLoader(one_file, strategy="fast")
        else:
            continue
        docs.extend(loader.load())
        shutil.move(one_file, KG_PROCESSED_DATA_PATH)
    embeddings = HuggingFaceEmbeddings(model_name=str(model))
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=150)
    split_docs = text_splitter.split_documents(docs)
    vectordb = Chroma.from_documents(documents=split_docs, embedding=embeddings,
                                     persist_directory=str(PERSISTENT_DIRECTORY))
    vectordb.persist()
