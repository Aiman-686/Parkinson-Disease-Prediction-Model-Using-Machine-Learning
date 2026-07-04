import streamlit as st
import numpy as np
import pickle
import os

# ==============================
# SAFE FILE LOADING (IMPORTANT)
# ==============================

BASE_DIR = os.path.dirname(__file__)

model_path = os.path.join(BASE_DIR, "parkinsons_model.sav")
scaler_path = os.path.join(BASE_DIR, "scaler.sav")

# Load model and scaler safely
try:
    model = pickle.load(open(model_path, "rb"))
    scaler = pickle.load(open(scaler_path, "rb"))
except Exception as e:
    st.error("❌ Model or scaler file not found. Please check GitHub deployment.")
    st.stop()

# ==============================
# UI
# ==============================

st.title("🧠 Parkinson Disease Prediction App")
st.write("Enter voice features in the sidebar")

st.sidebar.header("Input Features")

# Collect inputs
features = []

for i in range(22):
    val = st.sidebar.number_input(f"Feature {i+1}", value=0.0)
    features.append(val)

# ==============================
# PREDICTION
# ==============================

if st.button("Predict"):
    input_array = np.array(features).reshape(1, -1)

    try:
        input_scaled = scaler.transform(input_array)
        prediction = model.predict(input_scaled)

        if prediction[0] == 1:
            st.error("⚠️ Parkinson's Disease Detected")
        else:
            st.success("✅ No Parkinson's Disease Detected")

    except Exception as e:
        st.error("❌ Prediction failed. Check input or model compatibility.")