from pathlib import Path
import streamlit as st

st.set_page_config(page_title="About Spatial Proximity Excel Enrichment")


def read_markdown_file(markdown_file):
    text = Path(markdown_file).read_text()
    return text


# Example of embedding code using markdown 
st.markdown(read_markdown_file(r"assets\About_Proximity_Analysis.md"), unsafe_allow_html=True)

