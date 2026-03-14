import streamlit as st
import pickle

st.title("Iris Prediction")

model = pickle.load(open("model_iris.pkl", "rb"))

sl = st.slider("Sepal Length", 2.0, 10.0)
sw = st.slider("Sepal Width", 2.0, 10.0)
pl = st.slider("Petal Length", 2.0, 10.0)
pw = st.slider("Petal Width", 2.0, 10.0)

if st.button("Predict"):
    prediction = model.predict([[sl, sw, pl, pw]])
    st.success(f"Prediction: {prediction}")
