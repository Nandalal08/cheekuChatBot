#successfully implemented with history section

import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space
from hugchat import hugchat
from hugchat.login import Login

st.set_page_config(page_title="An LLM-powered Streamlit app")
    
# Sidebar contents
with st.sidebar:
    st.title("**Cheeku-Hamsa-yaar**")
    st.markdown('''
        ## About
        This is a Streamlit app that uses the HugChat API and an LLM (Language Model) from 
        the Hugging Face model to provide a fantastic chat experience. 
        so what's the wait for ... try the chekku Bot ❤️
    ''' )
    add_vertical_space(5)
    
    hf_email = st.text_input('Enter E-mail:', type='password')
    hf_pass = st.text_input('Enter password:', type='password')
    if not (hf_email and hf_pass):
        st.warning('Please enter your credentials!', icon='⚠️')
    else:
        st.success('Proceed to entering your prompt message!', icon='👉')
            
    st.write('Made cheeku with ❤️ by [nandxlal]')

# Generate empty lists for generated and past.
## generated stores AI generated responses
if 'generated' not in st.session_state:
    st.session_state['generated'] = ["I'm HugChat, How may I help you?"]
## past stores User's questions
if 'past' not in st.session_state:
    st.session_state['past'] = ['Hi!']

# Layout of input/response containers
input_container = st.container()
colored_header(label='', description='', color_name='blue-30')
response_container = st.container()

# User input

def get_text():
    input_text = st.text_input("You: ", "", key="input")
    return input_text
## Applying the user input box
with input_container:
    user_input = get_text()
# Log in to huggingface and grant authorization to huggingchat (enter creditionals)
email=hf_email
passwd=hf_pass
sign = Login(email, passwd)
cookies = sign.login()


# Response output

def generate_response(prompt):
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
    response = chatbot.chat(prompt)
    return response


with response_container:
    if user_input:
        response = generate_response(user_input)
        st.session_state.past.append(user_input)
        st.session_state.generated.append(response)
        
    if st.session_state['generated']:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))