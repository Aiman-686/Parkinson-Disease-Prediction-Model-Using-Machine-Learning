# 🧠 Parkinson Disease Prediction using Machine Learning

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge&logo=flask)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?style=for-the-badge&logo=scikitlearn)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

---

# 📖 Project Overview

Parkinson's Disease Prediction is a Machine Learning web application developed using **Python**, **Scikit-learn**, and **Flask**. The application predicts whether a person is likely to have Parkinson's disease based on biomedical voice measurements.

The project demonstrates the complete Machine Learning workflow, including data preprocessing, feature scaling, model training, evaluation, model serialization, and deployment as a web application.

This project is intended for educational purposes and demonstrates how Machine Learning can assist in disease prediction using voice-based biomedical features.

---

# 🧠 What is Parkinson's Disease?

Parkinson's disease (PD) is a **progressive neurological disorder** that primarily affects movement. It develops gradually as certain nerve cells (neurons) in the brain become damaged or die. These neurons produce dopamine, a chemical messenger responsible for coordinating smooth and balanced muscle movement.

As dopamine levels decrease, people begin experiencing movement-related problems along with several non-motor symptoms.

Although Parkinson's disease cannot currently be cured, early diagnosis and treatment can significantly improve the patient's quality of life.

---

# 📌 Common Symptoms

People suffering from Parkinson's disease may experience:

- Tremors (shaking of hands, fingers, or limbs)
- Slowed movement (Bradykinesia)
- Muscle stiffness
- Poor posture and balance
- Difficulty walking
- Soft or slurred speech
- Reduced facial expressions
- Difficulty writing
- Changes in handwriting
- Depression and anxiety
- Sleep disorders
- Loss of smell
- Cognitive impairment in advanced stages

Symptoms usually worsen gradually over time.

---

# ⚠️ Causes

The exact cause of Parkinson's disease remains unknown, but researchers believe it results from a combination of genetic and environmental factors.

Possible causes include:

- Loss of dopamine-producing neurons
- Genetic mutations
- Environmental toxins
- Aging
- Oxidative stress
- Protein accumulation in brain cells (Lewy bodies)

---

# 📈 Risk Factors

Several factors increase the risk of developing Parkinson's disease:

- Age (typically above 60 years)
- Family history
- Genetic mutations
- Exposure to pesticides
- Head injuries
- Environmental pollutants

---

# 🩺 Diagnosis

There is currently **no single laboratory test** that can definitively diagnose Parkinson's disease.

Doctors usually diagnose it using:

- Medical history
- Neurological examination
- Observation of movement
- Voice analysis
- MRI or CT scans (to rule out other conditions)
- Dopamine transporter imaging (DaTscan)

Machine Learning can assist doctors by identifying hidden patterns within patient data.

---

# 🎯 Objective

The objective of this project is to develop a Machine Learning model capable of predicting Parkinson's disease using biomedical voice measurements.

The trained model is deployed as a Flask web application, allowing users to input feature values and receive an instant prediction.

---

# 📊 Dataset Information

This project uses the **Parkinson's Disease Dataset** containing biomedical voice measurements.

Dataset Characteristics:

- Total Samples: **195**
- Healthy Individuals: **48**
- Parkinson's Patients: **147**
- Features Used: **22**
- Target Variable:
  - **0 → Healthy**
  - **1 → Parkinson's Disease**

The dataset contains various vocal frequency and signal processing measurements commonly used in Parkinson's disease research.

---

# 📋 Input Features

The model uses the following 22 features:

1. MDVP:Fo(Hz)
2. MDVP:Fhi(Hz)
3. MDVP:Flo(Hz)
4. MDVP:Jitter(%)
5. MDVP:Jitter(Abs)
6. MDVP:RAP
7. MDVP:PPQ
8. Jitter:DDP
9. MDVP:Shimmer
10. MDVP:Shimmer(dB)
11. Shimmer:APQ3
12. Shimmer:APQ5
13. MDVP:APQ
14. Shimmer:DDA
15. NHR
16. HNR
17. RPDE
18. DFA
19. Spread1
20. Spread2
21. D2
22. PPE

---

# 🤖 Machine Learning Workflow

The complete workflow includes:

- Data Collection
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Selection
- Feature Scaling using StandardScaler
- Train-Test Split
- Model Training
- Model Evaluation
- Model Serialization using Pickle
- Flask Deployment

---

# 🧮 Feature Scaling

Since the features have different numerical ranges, the dataset is standardized using **StandardScaler**.

Standardization improves model performance by ensuring every feature contributes equally during training.

---

# 🧠 Machine Learning Algorithm

This project uses the **Support Vector Machine (SVM)** classifier.

## Why SVM?

Support Vector Machine is well-suited for biomedical datasets because it:

- Performs well with high-dimensional data
- Handles non-linear boundaries effectively
- Produces robust classification results
- Generalizes well on small datasets
- Minimizes overfitting

---

# 🌐 Web Application

The trained model is deployed using **Flask**.

The web application allows users to:

- Enter all required voice measurements
- Submit feature values
- Receive an instant prediction
- Display whether Parkinson's disease is detected

---

# 🛠️ Technologies Used

- Python
- Flask
- NumPy
- Pandas
- Scikit-learn
- Pickle
- HTML5
- CSS3
- Bootstrap 5

---

# 📂 Project Structure
