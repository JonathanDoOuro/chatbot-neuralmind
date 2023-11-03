import streamlit as st
from domain.Chatbot import Chatbot

def main():
    st.title("Retrieval-Augmented Generation App")

    # Input field for API key
    api_key = st.text_input("Enter API Key:")
    
    if (api_key):
        st.success(f"API Key added with sucess.")
        chatbot = Chatbot(api_key=api_key) 

    question = st.text_area("Enter Text Question:")

    answer = ""

    if st.button("Generate Answer"):
        answer = chatbot.answer_question(question=question)

    st.text_area("Generated Answer:", answer, height=100)

if __name__ == "__main__":
    main()
