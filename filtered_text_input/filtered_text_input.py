
import streamlit.components.v1 as components
import os

_component_func = components.declare_component(
    "filtered_text_input",
    path=os.path.join(os.path.dirname(__file__), "frontend-react/build"),
)

def filtered_text_input(label="", key=None, default="", height=300):
    return _component_func(
        label=label,
        key=key,
        default=default,
        height=height,
    )

