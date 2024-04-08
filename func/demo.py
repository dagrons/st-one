import streamlit as st
import graphviz


def demo_page():
    st.color_picker("颜色选择器")
    st.progress(50, '进度')
    st.metric("Wind", "9 mph", "-8%")
    st.toast("你有一条消息待查收", icon='😍')

    with st.popover('popover'):
        st.text_input("popover")

    graph = graphviz.Digraph()
    graph.edge('run', 'intr')
    graph.edge('intr', 'runbl')
    graph.edge('runbl', 'run')
    graph.edge('run', 'kernel')
    graph.edge('kernel', 'zombie')
    graph.edge('kernel', 'sleep')
    graph.edge('kernel', 'runmem')
    graph.edge('sleep', 'swap')
    graph.edge('swap', 'runswap')
    graph.edge('runswap', 'new')
    graph.edge('runswap', 'runmem')
    graph.edge('new', 'runmem')
    graph.edge('sleep', 'runmem')
    st.graphviz_chart(graph)
