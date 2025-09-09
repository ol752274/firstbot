from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM
import streamlit as st
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Set environment variables safely
os.environ["LANGCHAIN_TRACING_V2"] = "true"
if os.getenv("LANGCHAIN_API_KEY"):
    os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# Prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please answer the user questions as best as you can."),
    ("user", "Question: {question}")
])

# Streamlit UI
st.title("Local LLM with Ollama and Streamlit")
input_text = st.text_input("Enter your question:")

# Use updated OllamaLLM
llm = OllamaLLM(model="gemma3:1b")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Run chain if user enters input
if input_text:
    result = chain.invoke({"question": input_text})
    st.write(result)
