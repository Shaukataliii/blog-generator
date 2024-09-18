# Author comment: I used gemma2:2b for blog generation because this was the only Ollama model I've downloaded. You can download any model from the Ollama Github and then use its name in line no: 18 while calling load_ollama_llm function.

import streamlit as st
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from time import time


BLOG_TEMPLATE = """
    Generate a blog for {purpose} on {blog_topic} with not more than {no_words}. Use a professional and informative tone.
    Don't provide invalid references or links.
    """

def generate_blog(blog_topic, no_words, purpose):
    print("Inside generate_blog..")
    s_time = get_current_time()

    llm = load_ollama_llm()
    prompt = prepare_prompt(blog_topic, no_words, purpose)
    blog = llm.invoke(prompt)

    e_time = get_current_time()
    time_taken = calculate_time_taken(s_time, e_time)

    return blog, time_taken

@st.cache_resource
def load_ollama_llm(model: str = 'gemma2:2b'):
    print("Inside load_ollama_llm..")
    llm = OllamaLLM(model=model)
    return llm

def prepare_prompt(blog_topic, no_words, purpose):
    print("Inside prepare_prompt..")
    prompt = load_prompt()
    prompt = prompt.format(purpose=purpose, blog_topic=blog_topic, no_words=no_words)
    return prompt

@st.cache_resource
def load_prompt():
    print("Inside load_prompt..")
    prompt = PromptTemplate(input_variables=['purpose', 'blog_topic', 'no_words'], template=BLOG_TEMPLATE)
    return prompt

def get_current_time():
    return time()

def calculate_time_taken(start_time, end_time):
    return f"{int(end_time - start_time)} s"