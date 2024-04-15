from pathlib import Path

import pandas as pd
import streamlit as st

from settings import TABLE_PATH


def gather_info_page():
    st.title("信息填报")
    st.markdown("信息填报，然后汇总，生成excel表单")
    form = st.form("信息填报")
    with form:
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("姓名")
            gender = st.radio("性别", ["男", "女"], horizontal=True)
            weight = st.slider("体重", 0, 1000)
        with col2:
            age = st.number_input("年龄", 0, 100)
            birthday = st.date_input("生日")
        submitted = st.form_submit_button("提交")
        if submitted:
            if not TABLE_PATH.exists():
                data = {
                    'name': [name],
                    'gender': [gender],
                    'weight': [weight],
                    'age': [age],
                    'birthday': [birthday],
                }
                df = pd.DataFrame(data)
                df.to_csv(TABLE_PATH, index=False)
            else:
                df = pd.read_csv(TABLE_PATH)
                data = {
                    'name': name,
                    'gender': gender,
                    'weight': weight,
                    'age': age,
                    'birthday': birthday,
                }
                df.loc[len(df)] = data
                df.to_csv(TABLE_PATH, index=False)
            st.toast("成功填报一条记录", icon='😍')
            st.balloons()
    df = pd.read_csv(TABLE_PATH)
    st.write(df)



