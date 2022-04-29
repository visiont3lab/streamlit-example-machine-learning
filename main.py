import joblib
import streamlit as st
import numpy as np


m =joblib.load("models/model_cross.pkl")
#m =joblib.load("models/model_fast.pkl")

st.title("Prediction Model")

age = st.slider('Age', 18, 65, 26)
num_hours = st.slider('Num Hours Working', 0, 12, 4)
experience = st.slider('Experience', 0, 5, 2)

X1 = age #  26 # 18-65
X2 = num_hours #4  # 0-12
X3 = experience #2   # 0-5

btn_run = st.button("Run")
if btn_run:
    X = np.array([X1,X2,X3])
    X = X.reshape(1,-1)

    Y_hat = m.predict(X)[0]

    st.write( "Prediciton salary: " + str(np.round(Y_hat,3)) )