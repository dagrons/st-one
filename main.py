import os

import dotenv
import streamlit as st
from streamlit_option_menu import option_menu

from func.chore.page.mortage_caculator import mortage_caculator
from func.llm_chatbot.page.llm_chatbot import llm_chatbot_page
from func.llm_chatbot.page.retriver import retrieval_page
from func.log_analyzer.page.log_analyzer import log_analyzer
from func.chart.page.vis import vis

if __name__ == "__main__":
    dotenv.load_dotenv()
    st.set_page_config(
        "One",
        page_title="one",
        page_icon="img/logo.png",
        initial_sidebar_state="expanded",
    )

    st.markdown(r"""
    <style>
       .stDeployButton{
               visibility: hidden
       }
       #MainMenu {
               visibility: hidden
       }
    </style>

    """, unsafe_allow_html=True)

    pages = {
        "QA问答": {
            "func": llm_chatbot_page,
        },
        "知识库检索": {
            "func": retrieval_page,
        },
        "数据可视化": {
            "func": vis,
        },
        "日志分析": {
            "func": log_analyzer,
        }
    }
    if st.query_params.get("mode") == "all":
        pages["房贷计算器"] = {
            "func": mortage_caculator,
        }
    with st.sidebar:
        st.image(
            os.path.join(
                "img", "logo.png"
            ),
            use_column_width=True
        )
        options = list(pages)
        default_index = 0
        selected_page = option_menu(
            None,
            options=options,
            default_index=default_index)
        st.markdown("""
        Keyword: 算法展示，数据可视化
        """)

    if selected_page in pages:
        pages[selected_page]['func']()
