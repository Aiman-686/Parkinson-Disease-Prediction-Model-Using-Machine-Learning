import streamlit as st
import numpy as np
import pickle
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

model_path = os.path.join(BASE_DIR, "parkinsons_model.sav")
scaler_path = os.path.join(BASE_DIR, "scaler.sav")

# load model + scaler
with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(scaler_path, "rb") as f:
    scaler = pickle.load(f)

st.title("🧠 Parkinson Disease Prediction App")
st.write("Enter voice features in sidebar")