import streamlit as st


def log_analyzer():
    st.title("日志分析")
    st.markdown("### 指定日志位置")
    log_path = st.text_input("日志位置", value="C:\\Users\\Administrator\\Desktop\\log")
    st.markdown("### 结果分析")
    st.write("结论")


