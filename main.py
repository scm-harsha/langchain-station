import streamlit as st
import llama_test as llama_func

st.title("Chat with Llama")

question = st.sidebar.text_area(label="What is your question?", max_chars=50)


response = llama_func.llm_func(question)
# response = llama_func.langchain_agent(question)
st.text(response)
