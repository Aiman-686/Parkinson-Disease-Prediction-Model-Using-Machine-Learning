import streamlit as st
import numpy as np
import pickle
import os

st.set_page_config(page_title="Parkinson App")

st.title("🧠 Parkinson Disease Prediction App")

# absolute path fix
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

model_path = os.path.join(BASE_DIR, "parkinsons_model.sav")
scaler_path = os.path.join(BASE_DIR, "scaler.sav")

# DEBUG (IMPORTANT)
st.write("📂 Files in runtime folder:", os.listdir(BASE_DIR))

# hard fail with clear message
if not os.path.exists(model_path) or not os.path.exists(scaler_path):
    st.error("❌ .sav files NOT found in deployed folder. GitHub/Streamlit sync issue.")
    st.stop()

model = pickle.load(open(model_path, "rb"))
scaler = pickle.load(open(scaler_path, "rb"))

st.success("✅ Model loaded successfully")