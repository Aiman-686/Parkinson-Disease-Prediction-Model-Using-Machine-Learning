import streamlit as st
import numpy as np
import pickle
import os

# ---------- Load model safely ----------
BASE_DIR = os.path.dirname(__file__)

model = pickle.load(open(os.path.join(BASE_DIR, "parkinsons_model.sav"), "rb"))
scaler = pickle.load(open(os.path.join(BASE_DIR, "scaler.sav"), "rb"))

# ---------- UI ----------
st.title("🧠 Parkinson Disease Prediction App")
st.write("Enter voice features in the sidebar")

# Sidebar inputs
st.sidebar.header("Input Features")

features = []

for i in range(22):
    val = st.sidebar.number_input(f"Feature {i+1}", value=0.0)
    features.append(val)

# ---------- Prediction ----------
if st.button("Predict"):
    input_array = np.array(features).reshape(1, -1)
    input_scaled = scaler.transform(input_array)
    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.error("⚠️ Parkinson's Disease Detected")
    else:
        st.success("✅ No Parkinson's Disease Detected")