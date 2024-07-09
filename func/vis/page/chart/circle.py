import numpy as np
import pandas as pd
import streamlit as st


def vis_circle():
    chart_data = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])
    st.vega_lite_chart(
        chart_data,
        {
            "mark": {"type": "circle", "tooltip": True},
            "encoding": {
                "x": {"field": "a", "type": "quantitative"},
                "y": {"field": "b", "type": "quantitative"},
                "size": {"field": "c", "type": "quantitative"},
                "color": {"field": "c", "type": "quantitative"},
            },
        },
    )
    st.code("""
            chart_data = pd.DataFrame(np.random.randn(200, 3), columns=["a", "b", "c"])
            st.vega_lite_chart(
                chart_data,
                {
                    "mark": {"type": "circle", "tooltip": True},
                    "encoding": {
                        "x": {"field": "a", "type": "quantitative"},
                        "y": {"field": "b", "type": "quantitative"},
                        "size": {"field": "c", "type": "quantitative"},
                        "color": {"field": "c", "type": "quantitative"},
                    },
                },
            )
            """)


if __name__ == "__main__":
    vis_circle()
