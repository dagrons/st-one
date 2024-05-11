import streamlit as st

from func.llm_chatbot.page.api import dummy_api, request_api
from func.llm_chatbot.server.model import KGType


def admin_page():
    model_mg, kg_mg = st.tabs(['模型管理', '知识库管理'])
    with model_mg:
        st.markdown("暂未支持")
    with kg_mg:
        upload_tab, mg_tab = st.tabs(['上传', '管理'])
        with upload_tab:
            with st.form("上传", border=False, clear_on_submit=True):
                c1, c2 = st.columns(2)
                with c1:
                    kg_db_type = st.selectbox('知识库类型', options=["chomradb"])
                with c2:
                    kg_db_name = st.text_input("知识库名称")
                kg_db_tarfile = st.file_uploader("上传格式需为tar.gz格式")
                submit = st.form_submit_button('上传', type="primary")
                if submit:
                    res = request_api.create_kg_db(kg_db_tarfile, kg_db_name, kg_db_type)
                    if res.ok:
                        st.balloons()
                        st.toast(f"{kg_db_name}上传成功")
                    else:
                        st.warning(f"上传失败, {res.json()['detail']}")
        with mg_tab:
            st.markdown("暂未支持")












