import streamlit as st
from domain.Chatbot import Chatbot

__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

def main():
    st.title("Chatbot para responder dúvidas sobre o vestibular da Unicamp 2024")

    # Input field for API key
    api_key = st.text_input("Coloque sua API KEY da OPEN AI:")
    
    if (api_key):
        st.success(f"API Key adicionada com sucesso")
        chatbot = Chatbot(api_key=api_key) 

    question = st.text_area("Faça uma pergunta:")

    answer = ""

    if st.button("Gerar resposta"):
        try:
            answer = chatbot.answer_question(question=question)
        except:
            st.error(f"API Key não valida")

    st.text_area("Resposta:", answer, height=max(100, int(len(answer) * 0.5)))

if __name__ == "__main__":
    main()
