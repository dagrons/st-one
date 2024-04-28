import os

import streamlit as st
from streamlit_option_menu import option_menu

from func.llm_chatbot.page.llm_agent import llm_agent_page
from func.llm_chatbot.page.llm_chatbot import llm_chatbot_page
from func.llm_chatbot.page.retriver import retrieval_page

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
        "问答机器人": {
            "func": llm_chatbot_page,
        },
        "智能助手": {
            "func": llm_agent_page,
        },
        "知识库检索": {
            "func": retrieval_page,
        }
    }

    with st.sidebar:
        st.image(
            os.path.join(
                "img", "nyan_cat.png"
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
        Keyword: 算法演示，个人助手，数据分析，可视化        
        """)

    if selected_page in pages:
        pages[selected_page]['func']()
