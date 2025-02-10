import streamlit as st
import requests

st.title("Chatbot")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for i, message in enumerate(st.session_state.messages):
    st.text_area(label=message["role"], value=message["content"], height=70, disabled=True, key=f"msg_{i}")

# User input field
user_input = st.text_input("Type a message...")

# Button click event
if st.button("Send") and user_input:
    st.session_state.messages.append({"role": "You", "content": user_input})

    # API request to chatbot
    response = requests.get(f"https://js.puter.com/v2/chat?text={user_input}")

    print("Raw response:", response.text)  # Debugging step

    try:
        data = response.json()
        bot_response = data.get("response", "Sorry, I didn't understand that.")
    except requests.exceptions.JSONDecodeError:
        bot_response = "Error: Unable to get a valid response from the chatbot."

    # Store chatbot response
    st.session_state.messages.append({"role": "Bot", "content": bot_response})
    
    # Force rerun to update chat
    st.rerun()

