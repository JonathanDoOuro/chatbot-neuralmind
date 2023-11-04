__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
import chromadb
from langchain.embeddings import OpenAIEmbeddings


class Retriever:
    def __init__(self, api_key):
        self.chroma_client = chromadb.PersistentClient(path="banco")
        self.collection = self.chroma_client.get_collection(name="textos_ada_nltk")
        self.model = OpenAIEmbeddings(openai_api_key=api_key, model_kwargs = {"model_name":"text-embedding-ada-002"})
    
    def _embed_query(self, query):
        return self.model.embed_query(query)
    
    def query_topK(self, query, n_results):
        embeddedQuery = self._embed_query(query)

        results = self.collection.query(
            query_embeddings = [embeddedQuery],
            n_results = n_results
        )

        topk = []

        for text in results['documents'][0]:
            topk.append(text)

        return topk

