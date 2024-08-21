from dotenv import load_dotenv
import os
import google.generativeai as genai
import streamlit as st
from PIL import Image
load_dotenv()
print(os.getenv("MY_EMAIL"))
print(os.getenv("MY_PASS"))
print(os.getenv("GOOGLE_API_KEY"))

API_KEY=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=API_KEY)
def get_gemini_response(input_messaage,input_image):
    model =genai.GenerativeModel("gemini-1.5-flash")
    if input_messaage!="":
        model.generate_content([input_message,input_image])
    else:
        response=model.generate_content([input_image])
    return response.txt   

st.set_page_config(page_title="Gemini based chatbot")
st.header("Gemini LLM Application ")

st.text_input("Input Prompt:",key="input")

uploaded_file = st.file_uploader("Choose an image:", type=['jpg', 'jpeg', 'png'])


image=""
if uploaded_file is not None:
    image= Image.open(uploaded_file)
    st.image(image,caption="uploaded image ")
submit=st.button("Submit")

if submit:
    response=get_gemini_response(input_messaage=input,input_image=image)
    st.subheader("your respone is :")
    st.write(response)