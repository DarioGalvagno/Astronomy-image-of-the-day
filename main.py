import streamlit as st
import requests


api_key = "hPYnOjd6PEWzGeNI8tXbIzh368psx1cOut5sCEB9"

url = "https://api.nasa.gov/planetary/apod?api_key=hPYnOjd6PEWzGeNI8tXbIzh368psx1cOut5sCEB9"

response = requests.get(url)
content = response.json()

title = content["title"]
image_url = content["url"]
explanation = content["explanation"]
date = content["date"]

image_filepath = "img.png"
response1 = requests.get(image_url)
with open(image_filepath, "wb") as file:
    file.write(response1.content)


st.title(title)
st.image(image_url)
st.write(explanation)
st.write(f"The picture was taken on the {date}")
st.write(f"**This page is developed by Dario Galvagno**")