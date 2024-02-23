import streamlit as st
import time
import marcus
import base64

# Streamlit setup
user = 'user.png'
bot = 'marcusImg.jpg'
st.set_page_config(page_title = 'M.A.R.C.U.S.', layout = 'centered', initial_sidebar_state = 'auto')

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('peach.jpg')   

st.title("M.A.R.C.U.S.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    role = message["role"]
    avatar = bot if role == "assistant" else user  # Change "user" to the actual user avatar

    with st.chat_message(role, avatar = avatar):
        st.markdown(message["content"])

if len(st.session_state.messages) == 0:
    # Display initial message from the bot
    initial_message = marcus.marcusInitial()
    with st.chat_message("assistant", avatar = bot):
        st.markdown(initial_message)
        st.session_state.messages.append({"role": "assistant", "content": initial_message})

# Accept user input
if prompt := st.chat_input("Feel free to express yourself..."):
    st.session_state.messages.append({"role": "user", "content": prompt})  # Add user message to chat history
    with st.chat_message("user", avatar=user):
        st.markdown(prompt)  # Display user message in chat message container

    # Call assistant_script.py to generate the response
    assistant_response = marcus.marcusChat(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant", avatar=bot):
        message_placeholder = st.empty()
        full_response = ""

        # Simulate stream of response with milliseconds delay
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            message_placeholder.markdown(full_response + "▌")  # Add a blinking cursor to simulate typing
        message_placeholder.markdown(assistant_response)

    st.session_state.messages.append({"role": "assistant", "content": full_response})  # Add assistant response to chat history

