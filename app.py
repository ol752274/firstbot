from langchain_openai import ChatOpenAI
from lanchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StructuredOutputParser

from streamlit as st
import os
from dotenv import load_dotenv

os.environ["OPENAI_API_KEY"] = "sk-..."
os.environ
load_dotenv()