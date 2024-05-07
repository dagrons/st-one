import streamlit as st


def admin_page():
    model_mg, kg_mg = st.tabs(['模型管理', '知识库管理'])
    with model_mg:
        upload_tab, register_tab, unregister_tab = st.tabs(['上传', '注册', '注销'])
    with kg_mg:
        upload_tab, register_tab, update_tab, unregister_tab = st.tabs(['上传', '注册', '更新', '注销'])
