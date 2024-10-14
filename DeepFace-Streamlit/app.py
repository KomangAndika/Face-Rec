import streamlit as st
from identify import *

st.set_page_config(page_title="Face Recog App", page_icon=":mahjong:")

def main():
    st.title("Face Recog App")
    st.divider()
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])


