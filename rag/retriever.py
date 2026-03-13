import faiss
from config.settings import settings
import numpy as np


class Retriever:

    def __init__(self, embeddings, chunks):

        self.chunks = chunks
        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatL2(dimension)
        self.index.add(embeddings)


    def retrieve(self, query_embedding):

        k = settings.TOP_K_RETRIEVAL

        distances, indices = self.index.search(query_embedding, k)

        results = [self.chunks[i] for i in indices[0]]

        return results