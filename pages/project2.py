# pages/project2.py
import streamlit as st

st.set_page_config(page_title="Project 2", layout="wide")

st.title("Project 2 AI enhanced GP tools in ArcGIS Pro ")
st.write("Description of Project 2")

# Example of embedding code using markdown
st.markdown("""
```python
def another_example_function():
    print("Hello, Streamlit!")
""")

st.markdown("""

<iframe width="560" height="315" src="https://www.youtube.com/embed/dQw4w9WgXcQ" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
""", unsafe_allow_html=True)
