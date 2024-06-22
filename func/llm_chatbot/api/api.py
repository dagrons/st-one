import json
import time
from abc import ABC, abstractmethod
from typing import List, Tuple, Iterator, Any, Dict, Union

import requests


class BaseAPI(ABC):

    @abstractmethod
    def stream_chat(self,
                    model: str,
                    prompt: str,
                    chat_history: List[Tuple[str, str]] = [],
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
    def search_kg_db(self,
                     query: str,
                     search_type: str,
                     search_kwargs: Dict[str, Any]) -> List[str]:
        ...


class DummyAPI(BaseAPI):

    def stream_chat(self, model: str, prompt: str, chat_history: List[Tuple[str, str]] = []) -> Iterator[
        Union[str, List[str]]]:
        yield ['dummy_source_documents']
        for i in range(10):
            time.sleep(1)
            yield 'dummy token'

    def search_kg_db(self, query: str, search_type: str, search_kwargs: Dict[str, Any]) -> List[str]:
        return [
            'dummy_recall'
        ] * 2


class RequestAPI(BaseAPI):
    endpoint = "http://localhost:8000"

    def stream_chat(self, model: str, prompt: str, chat_history: List[Tuple[str, str]] = []) -> Iterator[
        Union[str, List[str]]]:
        path = "/chat/generate"
        s = requests.Session()
        params = {
            "model": model,
            "prompt": prompt
        }
        with s.post(url=f"{self.endpoint}{path}", params=params, json=chat_history, stream=True) as resp:
            buffer = b""
            source_documents = ""
            in_source_documents = True
            for chunk in resp.iter_content(chunk_size=1, decode_unicode=False):
                if chunk:
                    buffer += chunk
                while buffer:
                    try:
                        char = buffer.decode("utf-8")
                        if in_source_documents:
                            source_documents += char
                            if source_documents.endswith("</docs>"):
                                source_documents = source_documents[:source_documents.find("</docs>")]
                                source_documents = source_documents[source_documents.find("<docs>") + len("<docs>"):]
                                yield json.loads(source_documents)
                                in_source_documents = False
                        else:
                            yield char
                        buffer = b""
                    except UnicodeDecodeError:
                        break

    def search_kg_db(self, query: str, search_type: str, search_kwargs: Dict[str, Any]) -> List[str]:
        path = '/search'
        s = requests.Session()
        params = {
            'search_type': search_type
        }
        with s.post(url=f"{self.endpoint}{path}", params=params, json={'query': query, 'search_kwargs': search_kwargs}) as resp:
            return resp.json()


dummy_api = DummyAPI()
request_api = RequestAPI()
