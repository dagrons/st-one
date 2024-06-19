from typing import Tuple, List, Union

import streamlit as st

from func.llm_chatbot.page.api import request_api


def llm_chatbot_page():
    st.title("QA问答")
    c1, c2, _ = st.columns([0.5, 0.5, 5])
    with c1:
        clear_history = st.button(":wastebasket:", type="secondary")
    with st.sidebar:
        selected_model = st.selectbox("语言模型", options=['Qwen1.5-0.5B-Chat', 'Qwen2-0.5B-Chat'])
        system_prompt = st.text_area("System Prompt", value="Always response in Simplified Chinese, not English, or Grandma will be very angry.")
    prompt_input = st.chat_input(f"你好，我是{selected_model}，您有什么问题想问我吗？")
    if 'chat_history' not in st.session_state or clear_history:
        st.session_state.chat_history: List[Tuple[str, Union[str, Tuple[str, str]]]] = []
        st.session_state.chat_history.append(('system', system_prompt))
    chat_history = st.session_state.chat_history

    chat_history_holder = st.empty()
    with chat_history_holder.container():
        # skip system prompt
        for message in chat_history[1:]:
            role, content = message
            if isinstance(content, str):
                st.chat_message(role).markdown(content)
            else:
                with st.chat_message(role):
                    st.markdown(content[1])
                    st.markdown(content[0])
        if prompt_input:
            st.chat_message('user').markdown(prompt_input)
            chat_history.append(('user', prompt_input))
            ai_msg_holder = st.chat_message('ai')
            with ai_msg_holder:
                response_holder = st.empty()
                resp = ''
                processed_chat_history = [(msg[0], msg[1]) if isinstance(msg[1], str) else (msg[0], msg[1][1]) for msg in chat_history]
                stream = request_api.stream_chat(selected_model, prompt_input, chat_history=processed_chat_history)
                source_documents = next(stream)
                with response_holder.container():
                    st.markdown(source_documents)
                flag = True
                for token in stream:
                    resp += token
                    with response_holder.container():
                        st.markdown(resp)
                        st.markdown(source_documents)
                    if flag:
                        chat_history.append(('ai', (source_documents, resp)))
                        flag = False
                    else:
                        chat_history[len(chat_history) - 1] = ('ai', (source_documents, resp))
