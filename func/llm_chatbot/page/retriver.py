import streamlit as st

from func.llm_chatbot.page.api import dummy_api, request_api


def retrieval_page():
    st.title("知识库检索")
    col1, col2 = st.columns([8, 1])
    with col1:
        prompt = st.text_input("输入你想检索的内容", label_visibility="collapsed")
    with col2:
        with st.popover(":hammer_and_wrench:"):
            search_type = st.selectbox("检索方式", options=['similarity_score_threshold', 'mmr', 'similarity'])
            if search_type == 'similarity':
                k = st.number_input('召回个数', min_value=0, max_value=100, value=4, step=1)
                search_kwargs = {'k': k}
            elif search_type == 'similarity_score_threshold':
                score = st.number_input('score threshold', min_value=-1000., max_value=1., value=-110., step=0.01)
                search_kwargs = {'score_threshold': score}
            else:
                k = st.number_input('召回个数', min_value=0, max_value=100, value=4, step=1)
                lambda_mult = st.number_input('lambda mult', min_value=0., max_value=100., value=0.25, step=0.01)
                search_kwargs = {'k': k, 'lambda_mult': lambda_mult}
    if prompt:
        result = request_api.search_kg_db(prompt, search_type, search_kwargs)
        st.write(result)
