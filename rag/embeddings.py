from sentence_transformers import SentenceTransformer
from config.settings import settings

class EmbeddingModel:

    def __init__(self):
        self.model = SentenceTransformer(settings.EMBEDDING_MODEL)

    def embed_texts(self, texts):
        return self.model.encode(texts)

    def embed_query(self, query):
        return self.model.encode([query])