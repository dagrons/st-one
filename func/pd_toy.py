import random

import pandas as pd
import streamlit as st
from faker import Faker
from streamlit_ace import st_ace


def pd_toy_page():
    st.title("PD测试器")
    N = 10
    M = 5
    random.seed(12)
    Faker.seed(0)
    fake = Faker("zh_CN")
    names = [fake.name() for _ in range(N)]
    # 个人信息
    st.markdown("#### df1")
    df1 = pd.DataFrame({
        'uid': [i for i in range(N)],
        "姓名": names,
        "头像": [fake.emoji() for _ in range(N)],
        "年龄": [random.randint(0, 99) for _ in range(N)],
        "工作": [fake.job() for _ in range(N)],
        "工资": [random.random() * 100000 for _ in range(N)],
        "专业": [random.choice(list('ABCDEFG')) for _ in range(N)],
        "住址": [fake.address() for _ in range(N)],
    })
    st.write(df1)
    col1, col2 = st.columns([5, 2])
    # posts
    with col1:
        st.markdown("#### df2")
        df2 = pd.DataFrame({
            'pid': [i for i in range(N*2)],
            "uid": [random.randint(0, N-1) for _ in range(N*2)],
            "Post": [fake.text() for _ in range(N*2)],
        })
        st.write(df2)
    with col2:
        # friends
        st.markdown("#### df3")
        df3 = pd.DataFrame({
            "follower": [random.randint(0, N-1) for _ in range(N*5)],
            "followed": [random.randint(0, N-1) for _ in range(N*5)],
        })
        st.write(df3)
    content = st_ace(value="""def solve(df1, df2, df3):
    pass""", language="python", keybinding="emacs")
    loc = {}
    glo = {'pd': pd}
    # glo传入全局变量
    # loc收集局部变量
    exec(content, glo, loc)
    st.write(loc['solve'](df1, df2, df3))


