import streamlit as st
import requests
from PIL import Image
import io
import os

st.title("Background Removal")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    if st.button("Remove Background"):
        with st.spinner("Processing..."):
            files = {"file": (uploaded_file.name, uploaded_file, "image/jpeg")}
            data = {"challenge": "cv3"}

            response = requests.post("http://localhost:8000/segment", files=files, data=data)

            if response.status_code == 200:
                result = response.json()
                if result["message"] == "succeed":
                    segmented_image_path = result["segmented_image_path"]
                    segmented_image = Image.open(segmented_image_path)
                    st.image(segmented_image, caption="Segmented Image", use_column_width=True)
                else:
                    st.error("Segmentation failed.")
            else:
                st.error(f"Error: {response.status_code}")