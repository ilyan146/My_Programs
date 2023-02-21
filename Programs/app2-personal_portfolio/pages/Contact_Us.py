import streamlit as st

st.title("Contact Me")

with st.form(key='email_forms'):
    email = st.text_input("Your Email Address")
    message = st.text_area("Your Message") #for multi line text
    submit_button = st.form_submit_button("Submit") #special button that acts as boolean.
    if submit_button:
        print("button was pressed!")