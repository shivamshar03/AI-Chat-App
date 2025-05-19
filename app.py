import streamlit as st
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini
# genai.configure(api_key="AIzaSyBGjYQIUiv5IBR6r51FvcDPaEnjN9M65Rg")
# Function to return the response
def load_answer(question):
    llm = ChatGroq(model_name="llama3-8b-8192")
    answer = llm.invoke(question)
    return answer.text

# Streamlit UI
st.set_page_config(page_title="LangChain Demo", page_icon= ":robot:")
st.header("LangChain Demo")

user_input = st.text_input("You: ")

if st.button("Generate") and user_input:
    with st.spinner("Generating answer..."):
        response = load_answer(user_input)
        st.subheader("Answer:")
        st.write(response)
