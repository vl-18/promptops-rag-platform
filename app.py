import streamlit as st

from rag.ingestion import DocumentIngestor
from rag.embeddings import EmbeddingModel
from rag.retriever import Retriever

from prompts.registry import get_prompt_framework, list_prompt_frameworks
from llm.client import LLMClient


st.title("PromptOps RAG Policy Assistant")

st.write("Ask questions about company policies.")

# Select prompt framework
framework_name = st.selectbox(
    "Choose Prompt Framework",
    list_prompt_frameworks()
)

# User question
query = st.text_input("Enter your question")


if st.button("Ask"):

    if query.strip() == "":
        st.warning("Please enter a question.")
    else:

        # ---- RAG PIPELINE ----

        ingestor = DocumentIngestor()

        documents = ingestor.load_documents()
        chunks = ingestor.create_chunks(documents)

        embedding_model = EmbeddingModel()

        chunk_texts = [chunk["content"] for chunk in chunks]
        embeddings = embedding_model.embed_texts(chunk_texts)

        retriever = Retriever(embeddings, chunks)

        query_embedding = embedding_model.embed_query(query)

        results = retriever.retrieve(query_embedding)

        context = "\n".join([r["content"] for r in results])

        # ---- PROMPT ENGINE ----

        prompt_framework = get_prompt_framework(framework_name)

        prompt = prompt_framework.build_prompt(
            query=query,
            context=context
        )

        # ---- LLM CALL ----

        llm = LLMClient()

        response = llm.generate(prompt)

        # ---- DISPLAY RESPONSE ----

        st.subheader("Answer")
        st.write(response)

        # ---- DISPLAY SOURCES ----

        st.subheader("Sources")

        for r in results:

            st.write("Source:", r["source"])
            st.write(r["content"])
            st.divider()