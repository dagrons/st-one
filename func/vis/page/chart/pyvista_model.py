import pyvista as pv
import stpyvista
import streamlit as st
from stpyvista.utils import start_xvfb


def vis_pyvista_model():
    if "IS_XVFB_RUNNING" not in st.session_state:
        start_xvfb()
        st.session_state.IS_XVFB_RUNNING = True

        # 创建一个示例网格
    mesh = pv.Sphere()

    # 创建一个 Plotter 对象
    plotter = pv.Plotter()

    # 向 Plotter 添加网格
    plotter.add_mesh(mesh, color="cyan")

    # 获取 Plotter 的摄像机位置
    plotter.show(cpos="xy")

    st.title("stpyvista Demo")
    stpyvista.show(plotter)
