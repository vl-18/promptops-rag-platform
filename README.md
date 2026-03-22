# 🤖 GenAI Policy Coach

A Retrieval-Augmented Generation (RAG) system designed to answer policy queries with grounded and explainable responses.

---

## 🚀 Features
- Modular RAG pipeline (ingestion, retrieval, generation)
- Supports multiple prompt frameworks: **CRISPE** and **CRAFT**
- 🔄 **Interactive UI to switch between prompt frameworks in real-time**
- Evaluation layer for response quality
- Streamlit-based interface for easy experimentation

---

## 🧠 Prompt Frameworks

This system enables users to dynamically select between two structured prompt engineering frameworks:

### 🔹 CRISPE
- **C**ontext
- **R**ole
- **I**nstruction
- **S**teps
- **P**arameters
- **E**xamples  

👉 Produces **detailed, structured, instruction-driven responses**

---

### 🔹 CRAFT
- **C**larify intent  
- **R**eason step-by-step  
- **A**nswer clearly  
- **F**ormat properly  
- **T**one appropriately  

👉 Produces **clear, concise, and well-structured responses**

---

## 🎛️ Interactive Framework Selection

Users can choose between **CRISPE** and **CRAFT** directly from the UI.

This allows:
- Understanding how prompt design impacts output quality
- Exploration of trade-offs between detail vs clarity

---

## 🔄 How it Works

1. User enters a query  
2. Relevant policy context is retrieved  
3. User selects a prompt framework (**CRISPE or CRAFT**) from the UI  
4. Response is generated using the selected framework  
5. Output is evaluated for quality metrics  

---

## 🧠 Key Insight

In enterprise AI systems, **prompt design is a first-class component**.

This project demonstrates how different prompt frameworks can significantly influence:
- Clarity
- Structure
- Usefulness of responses

---

## ⚖️ Trade-offs
- Mock LLM used for consistent demo experience
- Lightweight retrieval for simplicity
- Focus on prompt design and evaluation over model complexity

---

## 🧪 Sample Queries
- How many leave days are allowed?
- Can I work remotely full time?
- What is the reimbursement policy?

---

## ▶️ Run Locally
pip install -r requirements.txt  
streamlit run app.py