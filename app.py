import streamlit as st
import google.generativeai as genai

# Configure Gemini
genai.configure(api_key="YOUR_API_KEY")  # Replace with your actual key

# Initialize Gemini model
model = genai.GenerativeModel("gemini-1.5-pro-latest")

# Streamlit UI
st.set_page_config(page_title="Gemini Chatbot", page_icon=":robot:")
st.header("Hey, I'm your Gemini Assistant")

if "sessionMessages" not in st.session_state:
    st.session_state.sessionMessages = []

def load_answer(question):
    st.session_state.sessionMessages.append({"role": "user", "parts": [question]})

    response = model.generate_content(st.session_state.sessionMessages)

    st.session_state.sessionMessages.append({"role": "model", "parts": [response.text]})

    return response.text

def get_text():
    return st.text_input("You:")

user_input = get_text()

if st.button("Generate") and user_input:
    with st.spinner("Generating answer..."):
        response = load_answer(user_input)
        st.subheader("Answer:")
        st.write(response)
