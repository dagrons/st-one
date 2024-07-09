import plotly.express as px
import streamlit as st


def vis_pie():
    # 创建示例数据
    data = {
        'Category': ['A', 'B', 'C', 'D'],
        'Values': [4500, 2500, 1050, 500]
    }

    # 使用Plotly创建饼图并显示类别名称
    fig = px.pie(data, names='Category', values='Values', title='Sample Pie Chart')

    # 更新饼图以显示类别名称
    fig.update_traces(textinfo='label+percent', textposition='inside')

    # 在Streamlit中展示Plotly饼图
    st.plotly_chart(fig)
    st.code("""
        # 创建示例数据
    data = {
        'Category': ['A', 'B', 'C', 'D'],
        'Values': [4500, 2500, 1050, 500]
    }

    # 使用Plotly创建饼图并显示类别名称
    fig = px.pie(data, names='Category', values='Values', title='Sample Pie Chart')

    # 更新饼图以显示类别名称
    fig.update_traces(textinfo='label+percent', textposition='inside')

    # 在Streamlit中展示Plotly饼图
    st.plotly_chart(fig)

    """)
