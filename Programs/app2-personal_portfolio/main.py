import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("006 images\photo.png")

with col2:
    st.title("Mohamed Ilyan")
    content = """
    This is a trial content description and we will be making a nice summary of my experience and skillset here!!
    Also try to see how the content of this is displayed in the browser!!
    """
    st.info(content)

st.write("Below you find some of the apps I have built in Python, Feel free to contact me.")

df = pd.read_csv("006 data.csv")

col3, col4 = st.columns(2)

with col3:
    for index, row in df[0:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
