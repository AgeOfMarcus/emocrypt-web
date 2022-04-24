import streamlit as st
import requests

API = 'https://emocrypt-api.marcusweinberger.repl.co/api'
CHANNELS = ["pacer","trump","gamer","sus","amogus","shoulder","joe","random"]

st.title('Emocrypt')

st.write('''
### [Powered by emocrypt](https://github.com/degaart/emocrypt) - [@degaart](https://github.com/degaart)

This website was built with streamlit, and is hosted on replit. [View my source code!](/__repl)
''')

with st.form('encrypt'):
    st.write('Encrypt text:')
    
    channel = st.selectbox('Copypasta to use as mask', CHANNELS)
    text = st.text_area('Text to encrypt')
    password = st.text_input('Password', type='password')
    submitted = st.form_submit_button("Encrypt")

    if submitted:
        res = requests.post(f'{API}/encrypt', {
            'channel': channel,
            'password': password,
            'text': text
        }).json()
        if (res['ok']):
            st.write(res['result'])

with st.form('decrypt'):
    st.write('Decrypt ciphertext:')
    
    text = st.text_input('Encrypted text')
    password = st.text_input('Password', type='password')
    submitted = st.form_submit_button("Decrypt")

    if submitted:
        res = requests.post(f'{API}/decrypt', {
            'password': password,
            'text': text
        }).json()
        if (res['ok']):
            st.write(res['result'])