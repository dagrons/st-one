from abc import ABC, abstractmethod
from pathlib import Path
import time
from typing import List, Union, Tuple, Iterator, Any, Dict


class BaseAPI(ABC):

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
                    ) -> Union[Iterator[str|List[str]]]:
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
    def list_llm(self) -> List[str]:
        """

        :return:
        """
        ...

    @abstractmethod
    def list_kg_db(self) -> List[str]:
        """

        :return:
        """
        ...

    @abstractmethod
    def search_kg_db(self,
                     kg_name: str,
                     query: str,
                     search_type: str,
                     search_kwargs: Dict[str, Any]) -> List[str]:
        """

        :param kg_name:
        :param query:
        :param search_type:
        :param search_kwargs:
        :return:
        """
        ...


class DummyAPI(BaseAPI):

    def list_llm(self) -> List[str]:
        return ['dummy_model']

    def chat(self, model: str = "qwen:0.5b", kg_name: str = "m3e-base", chat_history: List[Tuple[str, str]] = [],
             enable_rag: bool = False) -> str|Tuple[str, str]:
        if enable_rag:
            return [('你也好'), ('source, 你好')]
        else:
            return '你也好'

    def stream_chat(self, model: str = "qwen:0.5b", kg_name: str = None,
                    chat_history: List[Tuple[str, str]] = [], enable_rag: bool = False) -> Union[
        Iterator[str|List[str]]]:
        if enable_rag:
            yield ['dummy_source_documents']
            for i in range(10):
                time.sleep(0.5)
                yield 'dummy token'
        for i in range(10):
            time.sleep(0.5)
            yield 'dummy token'

    def list_kg_db(self) -> List[str]:
        return ['dummy_kg']

    def search_kg_db(self, kg_name: str, query: str, search_type: str, search_kwargs: Dict[str, Any]) -> List[str]:
        return [
            'dummy_recall'
        ] * 2


api = DummyAPI()