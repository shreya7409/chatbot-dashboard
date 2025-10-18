import streamlit as st

st.set_page_config(page_title="Smart Chatbot", page_icon="💬", layout="centered")

st.title("💬Smart Chatbot Assisant")
st.write("Hey there! Ask me anything -- I'm here to help 😊")

if "messages" not in st.session_state:
  st.session_state["messages"] = []

for msg on st.session_state["messages"]:
st.write(msg)

user_input = st.text_input("Type your message...")

if user_input:

st.session_state["message"].append(f"**You:** {user_input}")

st.session_state["messages"].append(f"🤖Bot: I'm processing your question-smart replies coming soon!)

st.rerun()
