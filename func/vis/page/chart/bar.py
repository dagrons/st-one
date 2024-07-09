import plotly.graph_objects as go
import streamlit as st
import pandas as pd


def vis_bar():
    # 创建示例数据
    data = {
        'Category': ['A', 'B', 'C', 'D'],
        'Value1': [4500, 2500, 1050, 500],
        'Value2': [3000, 1500, 900, 400]
    }

    df = pd.DataFrame(data)

    mode = st.radio(
        "Bar Mode",
        ["stack", "group"],
        captions=["stack bar", "group bar"],
        horizontal=True,
    )
    # 创建Plotly图表对象
    fig = go.Figure()
    # 添加第一组柱状图
    fig.add_trace(go.Bar(x=df['Category'], y=df['Value1'], name='Value 1'))
    # 添加第二组柱状图
    fig.add_trace(go.Bar(x=df['Category'], y=df['Value2'], name='Value 2'))
    # 更新布局以堆叠柱状图
    fig.update_layout(barmode=mode, title='Stacked Bar Chart', xaxis_title='Category', yaxis_title='Values')

    # 在Streamlit中展示Plotly柱状图
    st.plotly_chart(fig)
    st.code("""
      # 创建示例数据
    data = {
        'Category': ['A', 'B', 'C', 'D'],
        'Value1': [4500, 2500, 1050, 500],
        'Value2': [3000, 1500, 900, 400]
    }

    df = pd.DataFrame(data)

    mode = st.radio(
        "Bar Mode",
        ["stack", "group"],
        captions = ["stack bar", "group bar"],
        horizontal=True,
    )
    # 创建Plotly图表对象
    fig = go.Figure()
    # 添加第一组柱状图
    fig.add_trace(go.Bar(x=df['Category'], y=df['Value1'], name='Value 1'))
    # 添加第二组柱状图
    fig.add_trace(go.Bar(x=df['Category'], y=df['Value2'], name='Value 2'))
    # 更新布局以堆叠柱状图
    fig.update_layout(barmode=mode, title='Stacked Bar Chart', xaxis_title='Category', yaxis_title='Values')

    # 在Streamlit中展示Plotly柱状图
    st.plotly_chart(fig)
    """)
