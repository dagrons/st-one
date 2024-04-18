import datetime

import pandas as pd
import streamlit as st

from settings import TODOCSV_PATH


def todolist_page():
    st.title("待办列表")
    with st.form('todolist', clear_on_submit=True):
        task = st.text_input('task')
        due = st.date_input('due')
        submit = st.form_submit_button()
        if submit:
            if not TODOCSV_PATH.exists():
                data = {
                    'task': [task],
                    'due': [due],
                    'status': ['todo'],
                    'finished_date': [None]
                }
                df = pd.DataFrame(data)
                df.to_csv(TODOCSV_PATH, index=False)
            else:
                data = {
                    'task': task,
                    'due': due,
                    'status': 'todo',
                    'finished_date': None,
                }
                df = pd.read_csv(TODOCSV_PATH)
                df.loc[len(df)] = data
                df.to_csv(TODOCSV_PATH, index=False)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### TODO")
        if TODOCSV_PATH.exists():
            df = pd.read_csv(TODOCSV_PATH)
            df = df.sort_values('due')
            for i in range(len(df)):
                if df.iloc[i, 2] == 'todo':
                    checked = st.checkbox(f"{df.iloc[i, 0]} / {df.iloc[i, 1]}", key=f'{i + 10}')
                    if checked:
                        df.iloc[i, 2] = 'done'
                        df.iloc[i, 3] = datetime.datetime.now()
                        df.to_csv(TODOCSV_PATH, index=False)
                        st.rerun()
    with col2:
        st.markdown("### DONE")
        if TODOCSV_PATH.exists():
            df = pd.read_csv(TODOCSV_PATH)
            df = df.sort_values('finished_date')
            for i in range(min(len(df), 10)):
                if df.iloc[i, 2] == 'done':
                    checked = st.checkbox(f"{df.iloc[i, 0]} / {df.iloc[i, 3]}", value=True, key=f'{i}')
                    if not checked:
                        df.iloc[i, 2] = 'todo'
                        df.iloc[i, 3] = None
                        df.to_csv(TODOCSV_PATH, index=False)
                        st.rerun()
