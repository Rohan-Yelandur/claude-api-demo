import anthropic
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

st.title("Claude Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []      # Saving messages allows Claude to remember conversation history.

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])     # Using markdown formats Claude's responses properly

if prompt := st.chat_input("Ask something..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=1024,
            messages=st.session_state.messages,
        )
        reply = response.content[0].text
        st.markdown(reply)

    st.session_state.messages.append({"role": "assistant", "content": reply})
