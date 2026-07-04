import streamlit as st
import numpy as np
import pickle
import os

# =====================
# LOAD MODEL
# =====================
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

model_path = os.path.join(BASE_DIR, "parkinsons_model.sav")
scaler_path = os.path.join(BASE_DIR, "scaler.sav")

with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(scaler_path, "rb") as f:
    scaler = pickle.load(f)

# =====================
# UI
# =====================
st.title("🧠 Parkinson Disease Prediction App")
st.write("Enter voice features in sidebar")

st.sidebar.header("Input Features")

features = np.array([
    st.sidebar.number_input(f"Feature {i+1}", 0.0)
    for i in range(22)
]).reshape(1, -1)

# =====================
# PREDICTION
# =====================
if st.button("Predict"):
    input_scaled = scaler.transform(features)
    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.error("⚠️ Parkinson's Disease Detected")
    else:
        st.success("✅ No Parkinson's Disease Detected")