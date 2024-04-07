# Import the libraries
import streamlit as st
from langchain.llms import OpenAI

# --------------------------------------------------------------------------------------------
# Add a suitable title for the application
st.title('🔓 OpenAI Access: Token-Powered Insights 🧠')

st.subheader("`Created by:` Aarish Khan and Asif Ali")
st.subheader("`Date:`  7th April 2024")

# ---------------------------------------------------------------------------------------------
# Providing a text input for the users
openai_api_key = st.sidebar.text_input('Provide the key of your OpenAI API here:')

# ---------------------------------------------------------------------------------------------
# Creating a func to get a result from the users
def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))

# ---------------------------------------------------------------------------------------------
# Creating a form for the users to type in their text
with st.form('my_form'):
  text = st.text_area('Begin your Input journey here by typing your Text:', '...')
  submitted = st.form_submit_button('Submit')
  
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter a valid OpenAI API Key!', icon='⚠')
    
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)

# ---------------------------------------------------------------------------------------------