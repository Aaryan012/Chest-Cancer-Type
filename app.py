import streamlit as st
from PIL import Image
import joblib
import numpy as np
import pandas as pd
import cv2
#load model
model=joblib.load('model.pt')
# Prediction function
def pred(img):
    # Convert into Grayscale
    img_gray=img.convert('L')
    # Resize into 100 100
    img_resize=img_gray.resize((100,100))
    # Convert to array and flatten
    img_arr=np.array(img_resize).flatten()
    # Convert to DataFrame and Transpose
    img_df=pd.DataFrame(img_arr).T
    # Prediction
    prediction=model.predict(img_df)
    return prediction
# upload image
st.title('Type of Chect Cancer Predictor')
file=st.file_uploader('Upload you file here',type='png')
# Read Image
try:
    if file is not None:
        # reads the image
        img=Image.open(file)
        # write image in web
        st.write('This is uploaded image',img)
        # mapping result
        label_img={0:'adenocarcinoma',1: 'large.cell.carcinoma', 2:'normal',3: 'squamous.cell.carcinoma'}
        img_pred=pred(img)
        img_pred=label_img[img_pred[0]]
        st.write('Your chest cancer type is :',img_pred)
    else:
        st.write("File cannot be read")
except Exception as e:
    st.write(f"{e} occured")
finally:
    st.write("Thank you for using service")