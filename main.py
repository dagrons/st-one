import os

import streamlit as st
from streamlit_option_menu import option_menu

import settings
from func.demo import demo_page
from func.gather_info import gather_info_page
from func.llm_chatbot.llm_chatbot import llm_chatbot_page
from func.pd_toy import pd_toy_page
from func.regex_test import regex_test_page
from func.todolist import todolist_page

if __name__ == "__main__":
    st.set_page_config(
        "One",
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
        "组件工厂": {
            "func": demo_page,
        },
        "待办列表": {
            "func": todolist_page
        },
        "信息填报": {
            "func": gather_info_page,
        },
        "正则测试器": {
            "func": regex_test_page,
        },
        "PD测试器": {
            "func": pd_toy_page,
        },
        "LLM Chatbot": {
            "func": llm_chatbot_page,
        }
    }

    with st.sidebar:
        st.image(
            os.path.join(
                "img", "one.png"
            ),
            use_column_width=True
        )
        options = list(pages)
        default_index = 0
        selected_page = option_menu(
            None,
            options=options,
            default_index=default_index)
        st.markdown("### 当前配置")
        st.write(settings.MODEL_PATH)
        st.markdown("""
        Repo: https://github.com/dagrons/one.git
        Keyword: 算法演示，个人助手，数据分析，可视化""")

    if selected_page in pages:
        pages[selected_page]['func']()
