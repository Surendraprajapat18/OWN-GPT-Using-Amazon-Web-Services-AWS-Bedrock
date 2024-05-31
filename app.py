import streamlit as st
import boto3
import json
import logging
import base64
import io
from PIL import Image
from botocore.exceptions import ClientError
from textGen import generate_text
from imageGen import generate_image, ImageError
from CodeGen import generate_code  

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger(__name__)

st.markdown("<h1 style='text-align: center;'>OWN GPT Using Bedrock</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Created by Surendra Prajapat</h4>", unsafe_allow_html=True)

# Create or retrieve session state
class SessionState:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

state = SessionState(search_history=[], text_results=[], image_results=[], code_results=[])

# Use markdown to create a smaller button
# st.markdown("<h3>Choose a service</h3>", unsafe_allow_html=True)
# service = st.radio("", ["Text Generation", "Image Generation", "Code Generation"])
service = st.selectbox("Choose a service", ["Text Generation", "Image Generation", "Code Generation"])


if service == "Text Generation":
    prompt = st.text_input("Enter your prompt for text generation:")
    if st.button("Generate Text"):
        if prompt:
            with st.spinner("Generating text..."):
                try:
                    result = generate_text(prompt)
                    state.text_results.append(result)
                    st.success("Text generated successfully!")
                except Exception as e:
                    st.error(f"Error generating text: {e}")
        else:
            st.error("Please enter a prompt.")

    # Display search history and results
    st.subheader("Text Generation History")
    for i, result in enumerate(state.text_results):
        st.write(f"Search {i + 1}:")
        st.write(result)

elif service == "Image Generation":
    prompt = st.text_input("Enter your prompt for image generation:")
    if st.button("Generate Image"):
        if prompt:
            with st.spinner("Generating image..."):
                model_id = 'stability.stable-diffusion-xl-v1'
                body = json.dumps({
                    "text_prompts": [
                        {"text": prompt}
                    ],
                    "cfg_scale": 10,
                    "seed": 0,
                    "steps": 50,
                    "samples": 1,
                    "style_preset": "photographic"
                })

                try:
                    image_bytes = generate_image(model_id=model_id, body=body)
                    state.image_results.append(image_bytes)
                    st.success("Image generated successfully!")
                except ClientError as err:
                    message = err.response["Error"]["Message"]
                    logger.error("A client error occurred: %s", message)
                    st.error(f"A client error occurred: {message}")
                except ImageError as err:
                    logger.error(err.message)
                    st.error(err.message)
                except Exception as e:
                    logger.error(f"An unexpected error occurred: {e}")
                    st.error(f"An unexpected error occurred: {e}")
    st.subheader("Image Generation History")
    for i, image_bytes in enumerate(state.image_results):
        st.write(f"Search {i + 1}:")
        image = Image.open(io.BytesIO(image_bytes))
        st.image(image, caption="Generated Image")

elif service == "Code Generation":
    prompt = st.text_input("Enter your prompt for code generation:")
    if st.button("Generate Code"):
        if prompt:
            with st.spinner("Generating code..."):
                try:
                    result = generate_code(prompt)
                    state.code_results.append(result)
                    st.success("Code generated successfully!")
                except Exception as e:
                    st.error(f"Error generating code: {e}")
        else:
            st.error("Please enter a prompt.")

    st.subheader("Code Generation History")
    for i, result in enumerate(state.code_results):
        st.write(f"Search {i + 1}:")
        st.code(result, language="python")  

