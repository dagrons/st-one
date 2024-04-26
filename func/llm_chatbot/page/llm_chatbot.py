import streamlit as st

from settings import SUPPORTED_MODELS, SUPPORTED_EMBEDDINGS


def llm_chatbot_page():
    st.title("LLM ChatBot")
    c1, c2, c3, c4 = st.columns([1, 1.5, 1.5, 1])
    with c1:
        clear_history = st.button("清空会话", type="primary")
    with c2:
        selected_model = st.selectbox("", options=SUPPORTED_MODELS, label_visibility="collapsed")
    with c3:
        selected_embedding = st.selectbox("", options=SUPPORTED_EMBEDDINGS, label_visibility="collapsed")
    with c4:
        with st.popover(":+1:"):
            enable_rag = st.checkbox("开启RAG")
            enable_show_ref = enable_rag and st.checkbox("显示召回")
            enable_history = st.checkbox("关联历史会话")
    messages_holder = st.empty()
    prompt_input = st.chat_input(f"你好，我是{selected_model}，您有什么问题想问我吗？")

