import pyvista as pv
import streamlit as st
from stpyvista import stpyvista
from stpyvista.utils import start_xvfb


def vis_pyvista_model():
    if "IS_XVFB_RUNNING" not in st.session_state:
        pv.start_xvfb()
        start_xvfb()
        st.session_state.IS_XVFB_RUNNING = True
    plotter = pv.Plotter(window_size=[200, 200])
    mesh = pv.Cube(center=(0, 0, 0))

    mesh['myscalar'] = mesh.points[:, 2] * mesh.points[:, 0]
    plotter.add_mesh(mesh, scalars='myscalar', cmap='bwr')

    plotter.view_isometric()
    plotter.background_color = 'white'

    # Send to streamlit
    stpyvista(plotter, key="pv_cube")
    st.code("""
    pv.start_xvfb()
    plotter = pv.Plotter(window_size=[400, 400])
    mesh = pv.Cube(center=(0, 0, 0))

    mesh['myscalar'] = mesh.points[:, 2] * mesh.points[:, 0]
    plotter.add_mesh(mesh, scalars='myscalar', cmap='bwr')
    
    plotter.view_isometric()
    plotter.background_color = 'white'
    
    # Send to streamlit
    stpyvista(plotter, key="pv_cube")
    """)
