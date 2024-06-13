import time
from abc import ABC, abstractmethod
from typing import List, Tuple, Iterator, Any, Dict, Union

from settings import SUPPORTED_MODEL_NAMES


class BaseAPI(ABC):
    @abstractmethod
    def chat(self,
             model: str = "qwen:0.5b",
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
    def search_kg_db(self,
                     query: str,
                     search_type: str,
                     search_kwargs: Dict[str, Any]) -> List[str]:
        ...


class DummyAPI(BaseAPI):

    def chat(self, model: str = "qwen:0.5b", chat_history: List[Tuple[str, str]] = [],
             enable_rag: bool = False) -> Union[str, Tuple[str, str]]:
        if enable_rag:
            return [('你也好'), ('source, 你好')]
        else:
            return '你也好'

    def stream_chat(self, model: str = "qwen:0.5b", chat_history: List[Tuple[str, str]] = [],
                    enable_rag: bool = False) -> Iterator[
        Union[str, List[str]]]:
        if enable_rag:
            yield ['dummy_source_documents']
            for i in range(10):
                time.sleep(1)
                yield 'dummy token'
        for i in range(10):
            time.sleep(1)
            yield 'dummy token'

    def search_kg_db(self, query: str, search_type: str, search_kwargs: Dict[str, Any]) -> List[str]:
        return [
            'dummy_recall'
        ] * 2


class RequestAPI(BaseAPI):
    endpoint = "http://localhost:8000"

    def chat(self, model: str = "qwen:0.5b", chat_history: List[Tuple[str, str]] = [],
             enable_rag: bool = False) -> Union[str, Tuple[str, str]]:
        pass

    def stream_chat(self, model: str = "qwen:0.5b", chat_history: List[Tuple[str, str]] = [],
                    enable_rag: bool = False) -> Iterator[Union[str, List[str]]]:
        pass

    def search_kg_db(self, query: str, search_type: str, search_kwargs: Dict[str, Any]) -> List[str]:
        pass


dummy_api = DummyAPI()
request_api = RequestAPI()
