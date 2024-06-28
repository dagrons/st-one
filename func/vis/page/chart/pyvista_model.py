import pyvista as pv
import streamlit as st
from stpyvista import stpyvista


def vis_pyvista_model():
    pv.start_xvfb()
    plotter = pv.Plotter(window_size=[400, 400])
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
