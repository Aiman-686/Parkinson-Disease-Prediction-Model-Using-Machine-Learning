import streamlit as st
import numpy as np
import pickle
import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

model_path = os.path.join(BASE_DIR, "parkinsons_model.sav")
scaler_path = os.path.join(BASE_DIR, "scaler.sav")

st.write("DEBUG: loading files...")

try:
    with open(model_path, "rb") as f:
        model = pickle.load(f)

    with open(scaler_path, "rb") as f:
        scaler = pickle.load(f)

    st.success("Model loaded successfully")

except Exception as e:
    st.error("❌ Pickle loading failed")
    st.exception(e)
    st.stop()