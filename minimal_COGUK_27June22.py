# -*- coding: utf-8 -*-


# load and evaluate a saved model
from numpy import loadtxt
from tensorflow.keras.models import load_model
import pandas as pd
# load model
model = load_model("june24_COGUK_model.h5")
# summarize model.
model.summary()

import streamlit as st

# Get the feature input from the user
def get_user_input():

    Sex      = st.sidebar.slider('Sex', 1, 2, 2)
    SNP_001457 = st.sidebar.slider('SNP_001457', 1, 4, 2)
    SNP_002480 = st.sidebar.slider('SNP_002480', 1, 4, 2)
    SNP_002558 = st.sidebar.slider('SNP_002558', 1, 4, 2)
    SNP_002875 = st.sidebar.slider('SNP_002875', 1, 4, 2)
    SNP_003037 = st.sidebar.slider('SNP_003037', 1, 4, 2)
    SNP_011287 = st.sidebar.slider('SNP_011287', 1, 4, 2)
    SNP_015406 = st.sidebar.slider('SNP_015406', 1, 4, 2)
    SNP_023403 = st.sidebar.slider('SNP_023403', 1, 4, 2)
    SNP_023923 = st.sidebar.slider('SNP_023923', 1, 4, 2)
      
    # Store a dictionary into a variable
    user_data ={'Sex': Sex,
                'SNP_001457': SNP_001457,
                'SNP_002480': SNP_002480,
                'SNP_002558': SNP_002558,
                'SNP_002875': SNP_002875,
                'SNP_003037': SNP_003037,
                'SNP_011287': SNP_011287,
                'SNP_015406': SNP_015406,
                'SNP_023403': SNP_023403,
                'SNP_023923': SNP_023923
                }

    #Transform the data into a data frame
    features = pd.DataFrame(user_data, index=[0])
    return features

# store the user's input into a variable
user_input = get_user_input()

#set a subheader and display the users input
#st.subheader('User input:')
#st.write(user_input)          # so when user puts in a value, we can see it on the app

st.header("COG-UK COVID SNP risk calculator") 
st.subheader("A project by UoP, UHS, UHP-QA and COG-UK")


y_new = model.predict(user_input)
#st.write(y_new)


if y_new > 0.226:
    st.write("**low RISK of DEATH**")    
elif y_new <= 0.226 :
    st.write("**probable RISK of DEATH predicted**")
    

st.write('')
st.write('Note: this model is not yet for approved clinical use')