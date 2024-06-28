import pyvista as pv
import pyvista.plotting
from stpyvista import stpyvista
import streamlit as st


def vis_pyvista_model():
    st.title("A cube")
    st.info("""Code adapted from https://docs.pyvista.org/user-guide/jupyter/pythreejs.html#scalars-support""")

    pv.start_xvfb()
    plotter = pv.Plotter(window_size=[400, 400])
    mesh = pv.Cube(center=(0, 0, 0))

    mesh['myscalar'] = mesh.points[:, 2] * mesh.points[:, 0]
    plotter.add_mesh(mesh, scalars='myscalar', cmap='bwr')

    plotter.view_isometric()
    plotter.background_color = 'white'

    # Send to streamlit
    stpyvista(plotter, key="pv_cube")
