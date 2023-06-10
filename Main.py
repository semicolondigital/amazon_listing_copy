import streamlit as st
from langchain.llms import OpenAI
from langchain import PromptTemplate
import os

template = """
    Write benefit-oriented Amazon Listing copy in {dialect} English according to this structure:
    - 1 product title
    - 5 benefit-oriented bullets that describes the features of the product (please use a bullet point format)

    Here is the product info: {product_info}
"""

prompt = PromptTemplate(
    input_variables=["product_info","dialect"],
    template=template,
)

st.set_page_config(page_title="Your Amazon Copywriter", page_icon=":tada:")
st.header("Your Amazon Copywriter")

st.markdown("Want to optimize your Amazon listings fast? Perfect! You're in the right place. Just paste your product information below and let us do the heavy lifing for you!")    

def get_api_key():
    api_key_input = st.text_input(label="Paste your API key here:", placeholder="Your API key goes here")
    return api_key_input

api_key = get_api_key()

if api_key:
    os.environ["OPENAI_API_KEY"] = api_key
    llm = OpenAI(temperature=.2)

st.markdown("## Paste your product info here:")

option_dialect = st.selectbox(
    "Which marketplace do you need copy for? (So that we use the right English.)",
    ("American","British"))

def get_text():
    input_text = st.text_area(label="", placeholder="Your product info goes here...")
    return input_text

product_input = get_text()

st.markdown("## Here's your optimized listing copy:")

if product_input:
    prompt_with_email = prompt.format(dialect=option_dialect, product_info=product_input)
    formatted_email = llm(prompt_with_email)
    st.write(formatted_email)