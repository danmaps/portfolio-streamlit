import requests
import streamlit as st

st.set_page_config(page_title="About Wordle Rainwater")


def read_markdown_url(url):
    response = requests.get(url,verify=False)
    return response.text


# Example of embedding code using markdown 
markdown_content = read_markdown_url("https://raw.githubusercontent.com/danmaps/wordle-rainwater/master/readme.md")
st.markdown(markdown_content, unsafe_allow_html=True)
