from typing import Tuple, List, Union

import streamlit as st
from pydantic import BaseModel

from func.llm_chatbot.page.api import dummy_api


class ChatHistoryItem(BaseModel):
    human_message: str
    ai_message: Union[str, Tuple[str, str]]


def llm_chatbot_page():
    st.title("QA问答")
    c1, c2, _ = st.columns([1.1, 1, 5])
    with c1:
        clear_history = st.button("清空会话", type="primary")
    with st.sidebar:
        kg_db_list = dummy_api.read_kg_dbs()
        llm_list = dummy_api.read_llms()
        selected_model = st.selectbox("语言模型", options=llm_list)
    with c2:
        with st.popover(":hammer_and_wrench:"):
            enable_rag = st.checkbox("开启RAG")
            enable_show_ref = enable_rag and st.checkbox("显示召回")
            enable_history = st.checkbox("关联历史会话")
    prompt_input = st.chat_input(f"你好，我是{selected_model}，您有什么问题想问我吗？")
    if 'chat_history' not in st.session_state or clear_history:
        st.session_state.chat_history: List[ChatHistoryItem] = []
    chat_history = st.session_state.chat_history

    msg_holder = st.empty()
    with msg_holder.container():
        for item in chat_history:
            if item is None:
                continue
            human_msg, ai_msg = item
            st.chat_message('user').markdown(human_msg)
            if isinstance(ai_msg, str):
                st.chat_message('assistant').markdown(ai_msg)
            else:
                with st.chat_message('assistant'):
                    st.markdown(ai_msg[0])
                    if enable_show_ref:
                        st.markdown(ai_msg[1])
        if prompt_input:
            chat_history.append(None)
            st.chat_message('user').markdown(prompt_input)
            msg = st.chat_message('assistant')
            with msg:
                placeholder = st.empty()
                resp = ''
                stream = dummy_api.stream_chat(selected_model, chat_history=[], enable_rag=enable_rag)
                if enable_rag:
                    source_documents = next(stream)
                for token in stream:
                    resp += token
                    placeholder.markdown(resp)
                    last_history_item = (prompt_input, (resp, source_documents) if enable_rag else resp)
                    chat_history[len(chat_history) - 1] = last_history_item
                if enable_show_ref:
                    st.markdown(source_documents)
