import streamlit as st

from func.vis.page.chart.bar import vis_bar
from func.vis.page.chart.circle import vis_circle
from func.vis.page.chart.line import vis_line
from func.vis.page.chart.pie import vis_pie
from func.vis.page.chart.scatter import vis_scatter


def vis():
    st.title("数据可视化")
    placeholder = st.empty()
    vis_funcs = {
        'circle': vis_circle,
        'scatter': vis_scatter,
        'pie': vis_pie,
        'line': vis_line,
        'bar': vis_bar,
    }
    vis_type = st.selectbox("类型", options=list(vis_funcs.keys()), label_visibility="collapsed")
    with placeholder.container():
        vis_funcs[vis_type]()
