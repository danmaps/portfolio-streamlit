# main.py
import streamlit as st

st.set_page_config(page_title="My Portfolio", layout="wide")

st.title("Welcome to My Portfolio")
st.write("Here you will find various projects that I have worked on.")

# List of projects with links
projects = [
    {"name": "Project 1", "link": "project1"},
    {"name": "Project 2", "link": "project2"},
    # Add more projects as needed
]

for project in projects:
    st.markdown(f"- [{project['name']}](/pages/{project['link']})")

st.write("Feel free to explore and learn more about each project!")

