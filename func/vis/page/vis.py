import streamlit as st

from func.vis.page.chart.circle import vis_circle


def vis():
    st.title("可视化")
    placeholder = st.empty()
    vis_type = st.selectbox("类型", options=['circle'], label_visibility="collapsed")
    vis_funcs = {
        'circle': vis_circle,
    }
    with placeholder.container():
        vis_funcs[vis_type]()
