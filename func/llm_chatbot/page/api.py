from typing import List, Union, Tuple, Iterator


class ApiRequest():
    def chat(self,
             model: str = "qwen:0.5b",
             emd_model: str = "m3e-base",
             chat_history: List[(str, str)] = [],
             enable_rag: bool = False,
             ) -> Union[str, Tuple[str, str]]:
        """
        聊天统一接口
        :param model: llm模型
        :param emd_model: 嵌入模型，用于rag
        :param chat_history:
        :param enable_rag:
        :return: str if only anwser, Tuple[str, str] if anwser and source_documents
        """

    def stream_chat(self,
                    model: str = "qwen:0.5b",
                    emd_model: str = "m3e-base",
                    chat_history: List[(str, str)] = [],
                    enable_rag: bool = False,
                    ) -> Union[Iterator[str], Tuple[Iterator[str], List[str]]]:
        """
        流式输出接口
        :param model:
        :param emd_model:
        :param chat_history:
        :param enable_rag:
        :return: iterator for anwser and list of source_documents
        """


