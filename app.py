import PIL
import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input_prompt, image_data):
    model=genai.GenerativeModel('gemini-1.5-flash')
    response=model.generate_content([input_prompt, image_data])
    return response.text
    
st.set_page_config(page_title="Food Calorie Counter")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image")

submit=st.button("Tell me about the total calories")

input_prompt="""
    You are an expert in nutritionist where you need to see the food items from the image
    and calculate the total calories, also provide the details of
    every food items with calories intake in below format

    1. Item 1 - no of calories
    2. Item 2 - no of calories
    ---
    ---

    Finally you can also mention whether the food is healthy or not and also
    mention the percentage split of the ration carbohydrates, fats, fibers, sugar and
    things required in our diet


"""

if submit:
    image_data = PIL.Image.open(uploaded_file)
    response=get_gemini_response(input_prompt,image_data)
    st.write(response)

