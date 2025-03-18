import streamlit as st
import time

st.title("AI Fitness Coach")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [
        {"sender": "bot", "text": "Hi! How can I help with your fitness journey today?"}
    ]

for message in st.session_state.chat_history:
    st.write(f"**{message['sender'].capitalize()}**: {message['text']}")

user_input = st.text_input("Ask the AI Coach...", key="chat_input")
if st.button("Send"):
    if user_input:
        st.session_state.chat_history.append({"sender": "user", "text": user_input})

        with st.spinner("Thinking..."):
            time.sleep(2)
            bot_response = ""
            st.session_state.chat_history.append({"sender": "bot", "text": bot_response})

        st.rerun()