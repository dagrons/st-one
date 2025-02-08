import plotly.graph_objects as go
import streamlit as st
import pandas as pd


def vis_line():
    # 创建示例数据
    data = {
        'Date': pd.date_range(start='2023-01-01', periods=10, freq='M'),
        'Value1': [10, 15, 13, 17, 22, 20, 19, 24, 30, 28],
        'Value2': [8, 12, 14, 16, 18, 23, 25, 27, 26, 30],
        'Value3': [5, 10, 12, 14, 18, 19, 22, 23, 25, 29]
    }

    df = pd.DataFrame(data)

    # 创建Plotly图表对象
    fig = go.Figure()
    # 添加第一条曲线
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Value1'], mode='lines+markers', name='Value 1',
                             marker=dict(size=8), line=dict(width=2)))
    # 添加第二条曲线
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Value2'], mode='lines+markers', name='Value 2',
                             marker=dict(size=8), line=dict(width=2)))
    # 添加第三条曲线
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Value3'], mode='lines+markers', name='Value 3',
                             marker=dict(size=8), line=dict(width=2)))
    # 更新布局
    fig.update_layout(title='Multiple Line Chart', xaxis_title='Date', yaxis_title='Values')

    # 在Streamlit中展示Plotly图表
    st.plotly_chart(fig)
    st.code("""
        # 创建示例数据
    data = {
        'Date': pd.date_range(start='2023-01-01', periods=10, freq='M'),
        'Value1': [10, 15, 13, 17, 22, 20, 19, 24, 30, 28],
        'Value2': [8, 12, 14, 16, 18, 23, 25, 27, 26, 30],
        'Value3': [5, 10, 12, 14, 18, 19, 22, 23, 25, 29]
    }

    df = pd.DataFrame(data)

    # 创建Plotly图表对象
    fig = go.Figure()
    # 添加第一条曲线
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Value1'], mode='lines+markers', name='Value 1',
                             marker=dict(size=8), line=dict(width=2)))
    # 添加第二条曲线
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Value2'], mode='lines+markers', name='Value 2',
                             marker=dict(size=8), line=dict(width=2)))
    # 添加第三条曲线
    fig.add_trace(go.Scatter(x=df['Date'], y=df['Value3'], mode='lines+markers', name='Value 3',
                             marker=dict(size=8), line=dict(width=2)))
    # 更新布局
    fig.update_layout(title='Multiple Line Chart', xaxis_title='Date', yaxis_title='Values')

    # 在Streamlit中展示Plotly图表
    st.plotly_chart(fig)
    """)
