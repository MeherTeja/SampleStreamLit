import streamlit as st
import requests
st.set_page_config(layout='wide')

st.title('TEXT-IMAGE GENERATION')


API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content
image_bytes = query({
	"inputs": st.text_input('Enter text','a photograph of astronaut riding  a horse'),
})
# You can access the image with PIL.Image for example
import io
from PIL import Image
image = Image.open(io.BytesIO(image_bytes))

if st.button("generate"):
	st.image(image)