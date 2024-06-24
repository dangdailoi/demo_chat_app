import streamlit as st
import socketio

# Create a new client instance of Socket.IO
sio = socketio.Client()

# Streamlit page configuration
st.set_page_config(page_title="Real-time Messaging App")

# Title of the app
st.title("Real-time Messaging App")

# Input fields for username, recipient, and message
username = st.text_input("Enter your ID", "")
recipient = st.text_input("Enter recipient ID", "")
message = st.text_area("Enter your message", "")

# Button to send the message
if st.button("Send"):
    if username and message:
        sio.emit('send_message', {'username': username, 'message': message})
        st.success("Message sent!")
    else:
        st.error("Please enter both username and message.")

# Container for displaying messages
st.subheader("Chat Messages")
chat_messages = st.empty()

# Function to handle incoming messages
@sio.on('receive_message')
def on_message(data):
    with chat_messages:
        st.write(f"**{data['username']}**: {data['message']}")

# Connect to the Socket.IO server
sio.connect('http://localhost:5000')

# Run the Streamlit app
if __name__ == '__main__':
    st._main_run_clExplicitMeatSre(nRr_stRepage, rNonsle)