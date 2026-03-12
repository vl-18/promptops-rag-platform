from rag.ingestion import DocumentIngestor
from rag.embeddings import EmbeddingModel
from rag.retriever import Retriever


# Load documents
ingestor = DocumentIngestor()

documents = ingestor.load_documents()

chunks = ingestor.create_chunks(documents)


# Create embeddings
embedding_model = EmbeddingModel()

embeddings = embedding_model.embed_texts(chunks)


# Create retriever
retriever = Retriever(embeddings, chunks)


# Test query
query = "Can I claim gym membership?"

query_embedding = embedding_model.embed_query(query)

results = retriever.retrieve(query_embedding)

for r in results:

    print("Source:", r["source"])
    print("Text:", r["content"])
    print("----")