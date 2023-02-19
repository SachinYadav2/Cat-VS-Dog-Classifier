import pickle
import streamlit as st
from PIL import Image
import os
import cv2
import numpy as np
from tensorflow.keras.models import load_model
model = load_model('model-1.h5')
# Your Page Title
st.title("Cat Vs Dog Classifier")

# UPload Image 
uploaded_image = st.file_uploader("Chose an Image")



def save_uploaded_image(uploaded_image):

    try:
        with open(os.path.join('uploads',uploaded_image.name),'wb') as f:
            f.write(uploaded_image.getbuffer())

        return (uploaded_image.name)
    except:
        return False

x = save_uploaded_image(uploaded_image)



if uploaded_image is not None:
    if save_uploaded_image(uploaded_image):
        display_image = Image.open(uploaded_image)
        m=st.image(display_image)
   
        def extract_features(img_path,model):


                test_img = cv2.imread(img_path)
                test_img = cv2.resize(test_img,(256,256))
                test_input = test_img.reshape((1,256,256,3))

                st.title("THIS IS YOUR OUPUT")
                x = int(model.predict(test_input)[0][0])
                if x == 1:
                    st.text("DOG")
                else:
                    st.text("CAT")




        uploaded = 'uploads'
        x = str(x)
        img_path = os.path.join(uploaded,x)
        img_path = str(img_path)
        extract_features(img_path,model)



