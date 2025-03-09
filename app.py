import streamlit as st
import google.generativeai as genai

# Set up your API key
GOOGLE_API_KEY = "AIzaSyDztytuLssyerVShZWvYow2BI7JZDuh1zI"
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the Gemini Pro model
model_name='gemini-2.0-flash'
model = genai.GenerativeModel(model_name)

# Streamlit UI
st.set_page_config(page_title="Chanakya - Google Gemini Chatbot", page_icon="🤖")

st.title("🤖 Google Gemini Chatbot - Chanakya")
# st.write("Chat with Google Gemini AI!")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Type your message...")

if user_input:
    # Display user message
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate Gemini AI response
    try:
        response = model.generate_content(user_input)
        bot_reply = response.text

        # Display AI response
        with st.chat_message("assistant"):
            st.markdown(bot_reply)

        # Save AI response to chat history
        st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    except Exception as e:
        st.error(f"Error: {e}")
