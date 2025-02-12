import streamlit as st

def fancy_markdown(text):
    """
    A function that converts the input text into paragraphs and renders them as HTML p tags with specified style.
    
    Parameters:
    text (str): The input text to be converted into paragraphs.
    
    Returns:
    None
    """
    
    st.markdown(text)#, unsafe_allow_html=True)
    
    # # split text by paragraph
    # text = text.split("\n")
    # # split text by paragraph 
    # for t in text:
    #     # put each paragraph in a p tag that is 50% width
    #     st.markdown(f"<p>{t}</p>", unsafe_allow_html=True)
    