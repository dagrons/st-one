import streamlit as st
from code_editor import code_editor


def demo_page():

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 常用组件")
        st.color_picker("颜色选择器")
        st.progress(50, '进度')
        st.metric("Wind", "9 mph", "-8%")
        st.toast("你有一条消息待查收", icon='😍')

        with st.popover('popover'):
            st.text_input("popover")
    with col2:
        st.markdown("""
        ### Graphviz        
        用于演示图相关的算法
        """)
        st.graphviz_chart('''
                    digraph G {
                        1 -> intr[color="red"]
                        intr -> runbl
                        runbl -> 1
                        1 -> kernel
                        kernel -> zombie
                        kernel -> sleep
                        kernel -> runmem
                        sleep -> swap
                        swap -> runswap
                        runswap -> new
                        runswap -> runmem
                        new -> runmem
                        sleep -> runmem
                    }''')
    with col1:
        st.markdown("""
        ### vega-lite        
        图表可视化        
        """)

    with col2:
        st.markdown("""
        ### pydeck
        地图可视化
        """)









