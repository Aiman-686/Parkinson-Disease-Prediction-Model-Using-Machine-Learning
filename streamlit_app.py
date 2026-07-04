import streamlit as st
import numpy as np
import pickle
import os

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(page_title="Parkinson Prediction", layout="centered")

st.title("🧠 Parkinson Disease Prediction App")
st.write("Enter voice features in the sidebar and click Predict")

# =========================
# FILE PATHS (SAFE)
# =========================
BASE_DIR = os.path.dirname(__file__)

model_path = os.path.join(BASE_DIR, "parkinsons_model.sav")
scaler_path = os.path.join(BASE_DIR, "scaler.sav")

# =========================
# LOAD MODEL SAFELY
# =========================
try:
    model = pickle.load(open(model_path, "rb"))
    scaler = pickle.load(open(scaler_path, "rb"))
except Exception:
    st.error("❌ Model files not found. Make sure .sav files are in GitHub ROOT folder.")
    st.stop()

# =========================
# SIDEBAR INPUTS
# =========================
st.sidebar.header("Input Features")

features = []

for i in range(22):
    val = st.sidebar.number_input(f"Feature {i+1}", value=0.0)
    features.append(val)

# =========================
# PREDICTION
# =========================
if st.button("Predict"):
    input_array = np.array(features).reshape(1, -1)

    try:
        input_scaled = scaler.transform(input_array)
        prediction = model.predict(input_scaled)

        if prediction[0] == 1:
            st.error("⚠️ Parkinson's Disease Detected")
        else:
            st.success("✅ No Parkinson's Disease Detected")

    except Exception:
        st.error("❌ Prediction failed. Check model compatibility.")