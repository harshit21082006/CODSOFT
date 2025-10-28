import streamlit as st
from chatbot import get_response

st.set_page_config(page_title="CodSoft Chatbot", page_icon="🤖")
st.title("🤖 CodSoft Rule-Based Chatbot")

# Session state to store chat history
if "history" not in st.session_state:
    st.session_state.history = []

# User input
user_input = st.text_input("You:", "")

if user_input:
    response = get_response(user_input)
    st.session_state.history.append({"user": user_input, "bot": response})

# Display chat history
for chat in st.session_state.history:
    st.markdown(f"**You:** {chat['user']}")
    st.markdown(f"**Bot:** {chat['bot']}")
    st.markdown("---")
