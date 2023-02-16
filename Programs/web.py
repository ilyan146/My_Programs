import streamlit as st
import functions

todos = functions.get_todos()

st.title("My Todo App")
st.subheader("This is my to do app.")
st.write("This app is to increase your productivity!")

for i in todos:
    st.checkbox(i)

st.text_input(label="", placeholder="Enter a todo....")


