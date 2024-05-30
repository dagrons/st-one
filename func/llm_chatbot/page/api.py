import io
import json
import time
from abc import ABC, abstractmethod
from typing import List, Tuple, Iterator, Any, Dict, Union

import requests

from func.llm_chatbot.server import schema
from settings import SUPPORTED_MODEL_NAMES


class BaseAPI(ABC):

    @abstractmethod
    def read_kg_dbs(self) -> List[schema.KGDB]:
        ...

    @abstractmethod
    def chat(self,
             model: str = "qwen:0.5b",
             kg_name: str = "m3e-base",
             chat_history: List[Tuple[str, str]] = [],
             enable_rag: bool = False,
             ) -> Union[str, Tuple[str, str]]:
        """
        聊天统一接口
        :param model: llm模型
        :param kg_name: 嵌入模型，用于rag
        :param chat_history:
        :param enable_rag:
        :return: str if only anwser, Tuple[str, str] if anwser and source_documents
        """
        ...

    @abstractmethod
    def stream_chat(self,
                    model: str = "qwen:0.5b",
                    kg_name: str = "m3e-base",
                    chat_history: List[Tuple[str, str]] = [],
                    enable_rag: bool = False,
                    ) -> Iterator[Union[str, List[str]]]:
        """
        流式输出接口
        :param model:
        :param kg_name:
        :param chat_history:
        :param enable_rag:
        :return: 当enable_rag时，第一个值为source_documents
        """
        ...

    @abstractmethod
    def read_llms(self) -> List[str]:
        ...

    @abstractmethod
    def search_kg_db(self,
                     kg_name: str,
                     query: str,
                     search_type: str,
                     search_kwargs: Dict[str, Any]) -> List[str]:
        ...


class DummyAPI(BaseAPI):

    def create_kg_db(self, uploaded_file: io.BytesIO, uploaded_filename: str, upload_kg_type):
        pass

    def read_llms(self) -> List[str]:
        return SUPPORTED_MODEL_NAMES

    def chat(self, model: str = "qwen:0.5b", kg_name: str = "m3e-base", chat_history: List[Tuple[str, str]] = [],
             enable_rag: bool = False) -> Union[str, Tuple[str, str]]:
        if enable_rag:
            return [('你也好'), ('source, 你好')]
        else:
            return '你也好'

    def stream_chat(self, model: str = "qwen:0.5b", kg_name: str = None,
                    chat_history: List[Tuple[str, str]] = [], enable_rag: bool = False) -> Iterator[
        Union[str, List[str]]]:
        if enable_rag:
            yield ['dummy_source_documents']
            for i in range(10):
                time.sleep(0.5)
                yield 'dummy token'
        for i in range(10):
            time.sleep(0.5)
            yield 'dummy token'

    def read_kg_dbs(self) -> Dict[str, bool]:
        return {'dummy_kg1': True, 'dummy_kg2': True, 'dummy_kg3': False}

    def search_kg_db(self, kg_name: str, query: str, search_type: str, search_kwargs: Dict[str, Any]) -> List[str]:
        return [
            'dummy_recall'
        ] * 2


class RequestAPI(BaseAPI):
    endpoint = "http://localhost:8000"

    def create_kg_db(self, uploaded_file: io.BytesIO, uploaded_filename: str, upload_kg_type: str):
        url = self.endpoint + '/kg_db/'
        data = {
            'item': json.dumps({
                'kg_name': uploaded_filename,
                'kg_type': upload_kg_type,
                'valid': False,
            })
        }
        files = {
            'kg_db_tarfile': (uploaded_filename, uploaded_file)
        }
        res = requests.post(url, data=data, files=files)
        return res

    def chat(self, model: str = "qwen:0.5b", kg_name: str = "m3e-base", chat_history: List[Tuple[str, str]] = [],
             enable_rag: bool = False) -> Union[str, Tuple[str, str]]:
        pass

    def stream_chat(self, model: str = "qwen:0.5b", kg_name: str = "m3e-base", chat_history: List[Tuple[str, str]] = [],
                    enable_rag: bool = False) -> Iterator[Union[str, List[str]]]:
        pass

    def read_llms(self) -> List[str]:
        return SUPPORTED_MODEL_NAMES

    def read_kg_dbs(self) -> List[schema.KGDB]:
        url = self.endpoint + '/kg_dbs/'
        res = requests.get(url)
        return [schema.KGDB.model_validate(item) for item in res.json()]

    def search_kg_db(self, kg_name: str, query: str, search_type: str, search_kwargs: Dict[str, Any]) -> List[str]:
        pass


dummy_api = DummyAPI()
request_api = RequestAPI()
