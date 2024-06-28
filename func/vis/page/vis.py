import streamlit as st

from func.vis.page.chart.circle import vis_circle


def vis():
    st.title("可视化")
    placeholder = st.empty()
    vis_funcs = {
        'circle': vis_circle,
    }
    vis_type = st.selectbox("类型", options=list(vis_funcs.keys()), label_visibility="collapsed")
    with placeholder.container():
        vis_funcs[vis_type]()
