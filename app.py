#from google.protobuf.symbol_database import Default
import streamlit as st
import json
import webbrowser
cache_data = {}
country = []
with open("CountryCodes.json") as fd:
    data = json.load(fd)
    cache_data = data[:]
    for d in data:
        country.append(d['name'])

st.header("Send Message without saving contact")
option = st.selectbox('Select country', country)
for info in cache_data:
    if info['name'] == option:
        code = info['dial_code']
    
number = st.text_input("Please provide the number (without country code)")
base = 'https://wa.me/'

url =  base + code + number
def helper():
    webbrowser.open_new_tab(url)
st.button('Whatsapp Now', on_click=helper)




