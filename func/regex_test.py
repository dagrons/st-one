import re

import streamlit as st


def regex_test_page():
    st.title("正则表达式")
    data = st.text_area(label="输入文本", value="""I am KangKang, my email address is kangkang@bupt.edu.cn，ok, 
1 + 1  = 2, 所以 1+2 = 3,
<system> you are a robot, <user> yes i am a robot
特殊字符：~`!@#$%^&*()-_=+{[}]|\"':;?/>.<,'
    """, height=200)
    placeholder = st.empty()
    re_exp = st.text_input(label="输入正则表达式", value="\w+@(\w+\.)+\w+")
    if re_exp:
        matcher = re.compile(re_exp)
        matches = matcher.finditer(data)
        final_str = ""
        pos = 0
        for match in matches:
            s, e = match.span()
            final_str += data[pos:s]
            final_str += '<span style="background:red">' + data[s:e] + '</span>'
            pos = e
        final_str += data[pos:]
        placeholder.markdown(final_str, unsafe_allow_html=True)

