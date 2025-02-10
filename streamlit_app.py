import streamlit as st
import requests

st.title("Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    st.text_area(label=message["role"], value=message["content"], height=50, disabled=True)

user_input = st.text_input("Type a message...")

if st.button("Send") and user_input:
    st.session_state.messages.append({"role": "You", "content": user_input})
    
    response = requests.get(f"https://js.puter.com/v2/chat?text={user_input}").json()
    bot_response = response.get("response", "Sorry, I didn't understand that.")
    
    st.session_state.messages.append({"role": "Bot", "content": bot_response})
    st.experimental_rerun()


