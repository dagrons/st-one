import plotly.express as px
import streamlit as st


def vis_scatter():
    # 创建示例数据
    df = px.data.iris()
    # 使用Plotly创建交互式散点图
    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                     title="Interactive Iris Scatter Plot")
    # 在Streamlit中展示Plotly图表
    st.plotly_chart(fig)
    st.code("""import plotly.express as px
import streamlit as st

# 创建示例数据
df = px.data.iris()

# 使用Plotly创建交互式散点图
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 title="Interactive Iris Scatter Plot")

# 在Streamlit中展示Plotly图表
st.plotly_chart(fig)

    """)
