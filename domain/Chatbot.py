from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from domain.Retriever import Retriever

class Chatbot:
    def __init__(self, api_key):
        self.chat = ChatOpenAI(openai_api_key=api_key,
                                max_tokens=250,
                                model = "gpt-3.5-turbo",
                                temperature=0.1)
        
        self.prompt = PromptTemplate.from_template(
            """Considering these texts as context: {context}.
            Give me a brilliant answer to the following question: {question}

            Make sure to answer using Portuguese language.""")
        
        self.chain = self.prompt | self.chat

        self.retriever = Retriever(api_key = api_key)

    def dummy(self, q):
        return "essa é uma resposta padrão"

    def _get_context(self, question):
        retrieved_texts = self.retriever.query_topK(query = question, n_results = 10)

        return "\n".join(retrieved_texts)

    def answer_question(self, question):

        context = self._get_context(question)

        response = self.chain.invoke({"context": context, "question": question})

        answer = response.content

        return answer

