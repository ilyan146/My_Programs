import streamlit as st
from send_email import send_email

st.title("Contact Me")

with st.form(key='email_forms'):
    email = st.text_input("Your Email Address")
    message = st.text_area("Your Message") #for multi line text
    raw_message = f"""\
Subject: Email from portfolio

From: {email}
{message}
"""
    submit_button = st.form_submit_button("Submit") #special button that acts as boolean.
    if submit_button:
        send_email(raw_message)
        st.info("Your message has been sent")