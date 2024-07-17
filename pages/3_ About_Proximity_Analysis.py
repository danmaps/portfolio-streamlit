# pages/project1.py
from pathlib import Path
import streamlit as st

st.set_page_config(page_title="About Spatial Proximity Excel Enrichment", )#layout="wide")


def read_markdown_file(markdown_file):
    text = Path(markdown_file).read_text()
    return text


# Example of embedding code using markdown 
st.markdown(read_markdown_file(r"pages/spatial_analysis_blog_post.md"), unsafe_allow_html=True)

