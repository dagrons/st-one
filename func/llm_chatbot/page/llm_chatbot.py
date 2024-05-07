from typing import Tuple, List

import streamlit as st

from func.llm_chatbot.page.api import api


def llm_chatbot_page():
    st.title("QA问答")
    c1, c2, _ = st.columns([1, 1, 5])
    with c1:
        clear_history = st.button("清空会话", type="primary")
    with st.sidebar:
        kg_db_list = api.list_kg_db()
        llm_list = api.list_llm()
        selected_model = st.selectbox("语言模型", options=llm_list)
        selected_db = st.selectbox("数据库", options=kg_db_list)
    with c2:
        with st.popover(":hammer_and_wrench:"):
            enable_rag = st.checkbox("开启RAG")
            enable_show_ref = enable_rag and st.checkbox("显示召回")
            enable_history = st.checkbox("关联历史会话")
    prompt_input = st.chat_input(f"你好，我是{selected_model}，您有什么问题想问我吗？")
    if 'chat_history' not in st.session_state or clear_history:
        st.session_state.chat_history: List[Tuple[str, Tuple[str, str]|str]]= []
    chat_history = st.session_state.chat_history
    msg_holder = st.empty()
    with msg_holder.container():
        for user_msg, assistant_msg in chat_history:
            st.chat_message('user').markdown(user_msg)
            if isinstance(assistant_msg, str):
                st.chat_message('assistant').markdown(assistant_msg)
            else:
                with st.chat_message('assistant'):
                    st.markdown(assistant_msg[0])
                    if enable_show_ref:
                        st.markdown(assistant_msg[1])
        if prompt_input:
            st.chat_message('user').markdown(prompt_input)
            msg = st.chat_message('assistant')
            with msg:
                placeholder = st.empty()
                resp = ''
                stream = api.stream_chat(selected_model, selected_db, chat_history=[], enable_rag=enable_rag)
                if enable_rag:
                    source_documents = next(stream)
                for token in stream:
                    resp += token
                    placeholder.markdown(resp)
                if enable_show_ref:
                    st.markdown(source_documents)
                chat_history.append((prompt_input, (resp, source_documents) if enable_rag else resp))




