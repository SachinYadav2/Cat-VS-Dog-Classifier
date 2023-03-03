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
    col1,col2 = st.columns(2)
    if save_uploaded_image(uploaded_image):
        display_image = Image.open(uploaded_image)

        with col1:
            st.header('Your uploaded image')
            
            m=st.image(display_image,width=300)
   
        def extract_features(img_path,model):


                test_img = cv2.imread(img_path)
                test_img = cv2.resize(test_img,(256,256))
                test_input = test_img.reshape((1,256,256,3))

                x = int(model.predict(test_input)[0][0])

                with col2:
                    if x == 1:
                        
                        st.header("Your Image like this")
                        st.text("DOG")
                        display_image = Image.open('show/dog.jpg')
                        return st.image(display_image,width=300)
                    else:
                        st.header("Your Image like this")
                        st.text("CAT")
                        display_image = Image.open('show/cat.jpeg')
                        return st.image(display_image,width=300)




        uploaded = 'uploads'
        x = str(x)
        img_path = os.path.join(uploaded,x)
        img_path = str(img_path)
        extract_features(img_path,model)



