import streamlit as st
from streamlit import spinner

from func.llm_chatbot.page.api import api


def retrieval_page():
    st.title("知识库检索")
    with st.sidebar:
        with spinner("正在获取数据库列表"):
            kg_db_list = api.list_kg_db()
        selected_kg_name = st.selectbox('数据库', options=kg_db_list)
    col1, col2 = st.columns([8, 1])
    with col1:
        prompt = st.text_input("输入你想检索的内容", label_visibility="collapsed")
    with col2:
        with st.popover(":hammer_and_wrench:"):
            search_type = st.selectbox("检索方式", options=['similarity', 'similarity_score_threshold', 'mmr'])
            if search_type == 'similarity':
                k = st.number_input('召回个数', min_value=0, max_value=100, value=4, step=1)
                search_kwargs = {'k': k}
            elif search_type == 'similarity_score_threshold':
                score = st.number_input('score threshold', min_value=-1000., max_value=1., value=-100., step=0.01)
                search_kwargs = {'score_threshold': score}
            else:
                k = st.number_input('召回个数', min_value=0, max_value=100, value=4, step=1)
                lambda_mult = st.number_input('lambda mult', min_value=0., max_value=100., value=0.25, step=0.01)
                search_kwargs = {'k': k, 'lambda_mult': lambda_mult}
    if prompt:
        result = api.search_kg_db(selected_kg_name, prompt, search_type, search_kwargs)
        st.write(result)
