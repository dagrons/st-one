import time

import pandas as pd
import streamlit as st

from settings import LOG_PATH


def process(data_path):
    df = pd.read_excel(data_path)
    return df


def log_tool_page():
    st.title("日志分析小工具")

    st.markdown("""
    - 首先你需要指定日志目录路径
    - 然后点击分析按钮
    - 分析完毕后，会出现分析结果
    """)

    st.markdown("### 指定路径&开始分析")

    data_path = st.text_input(label="请指定日志目录路径",
                              value=LOG_PATH)

    confirmed = st.button(label="开始分析")

    st.markdown("### 分析结果")

    placeholder = st.empty()
    if confirmed and data_path:
        with placeholder:
            with st.spinner("任务执行中，请耐心等待..."):
                time.sleep(2)
                res = process(data_path)
        st.session_state.res = res
        with placeholder:
            st.write(res)

    elif "res" in st.session_state:
        with placeholder:
            st.write(st.session_state.res)


