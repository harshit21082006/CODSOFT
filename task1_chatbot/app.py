# app.py
import streamlit as st
from chatbot import get_response

st.set_page_config(page_title="CodSoft Chatbot", page_icon="🤖")
st.title("🤖 CodSoft Chatbot")

st.markdown("Type a message below and get a response!")

user_input = st.text_input("You:")
if user_input:
    response = get_response(user_input)
    st.text_area("Chatbot:", value=response, height=100)
