import streamlit as st
import google.generativeai as genai


st.title("Welcome to Gemini chatbot")

genai.configure(api_key="AIzaSyD0AJ42-kPJkv_dueFv8wS2xoXpOvnOtmU")

text = st.text_input("Enter a message")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

if st.button("Search"):
    response = chat.send_message(text)
    st.write(response.text)
