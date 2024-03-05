import streamlit as st
from fastai.vision.all import *
#import plotly.express as px 

import pathlib
temp=pathlib.PosixPath
pathlib.PosixPath=pathlib.WindowsPath



#title
st.title("Vegetables and Fruit Classification")

#upload images
file=st.file_uploader("Rasm yuklash",type=["png","jpeg","gif","svg"])
if file:
    st.image(file) # >> rasmni chiqarish uchun

    # PIL convert >> rasmni raqamga aylantirish
    img=PILImage.create(file)

    #predict model
    model=load_learner("food_class.pkl")

    # prediction
    pred,pred_id,prob=model.predict(img)

    st.success(pred)
    st.info(f"Ehtimollik: {prob[pred_id]*100:.2f}%")
    
    
    # plotting
    # fig=px.bar(x=prob*100,y=model.dls.vocab)
    # st.plotly_chart(fig)