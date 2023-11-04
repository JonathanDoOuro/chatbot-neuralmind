from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from domain.Retriever import Retriever

import time

class Chatbot:
    def __init__(self, api_key):
        self.chat = ChatOpenAI(openai_api_key=api_key,
                                max_tokens=250,
                                model = "gpt-3.5-turbo",
                                temperature=0.1)
        
        self.prompt = PromptTemplate.from_template(
            """Contexto: {context}.
            Pergunta: {question}.
            
            Resposta: """)
        
        self.chain = self.prompt | self.chat

        self.retriever = Retriever(api_key = api_key)

    def dummy(self, q):
        return "essa é uma resposta padrão"

    def _get_context(self, question):
        retrieved_texts = self.retriever.query_topK(query = question, n_results = 10)

        return "\n".join(retrieved_texts)

    def answer_question(self, question):

        inicio = time.time()
        context = self._get_context(question)
        fim = time.time()

        print("tempo de buscar os textos: ", fim - inicio)

        inicio = time.time()
        response = self.chain.invoke({"context": context, "question": question})
        fim = time.time()
        print("tempo de buscar responder: ", fim - inicio)

        answer = response.content

        return answer

