import streamlit as st

from rag.ingestion import DocumentIngestor
from rag.embeddings import EmbeddingModel
from rag.retriever import Retriever
from evaluation.evaluator import Evaluator

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
        evaluator = Evaluator(llm)

        result = llm.generate(prompt)

        response = result["response"]
        tokens = result["tokens"]
        latency = result["latency"]

        metrics = evaluator.evaluate_all(
        query=query,
        context=context,
        response=response,
        latency=latency,
        tokens=tokens
)

        # ---- DISPLAY RESPONSE ----

        st.subheader("Answer")
        st.write(response)

        st.subheader("Metrics")

        st.write(f"Relevance: {metrics['relevance']}")
        st.write(f"Faithfulness: {metrics['faithfulness']}")
        st.write(f"Latency: {round(metrics['latency'], 2)} sec")
        st.write(f"Tokens: {metrics['tokens']}")

        with st.expander("Evaluation Details"):
            st.write("Relevance Reason:", metrics["details"]["relevance_reason"])
            st.write("Faithfulness Reason:", metrics["details"]["faithfulness_reason"])

        # ---- DISPLAY SOURCES ----

        st.subheader("Sources")

        for r in results:

            st.write("Source:", r["source"])
            st.write(r["content"])
            st.divider()