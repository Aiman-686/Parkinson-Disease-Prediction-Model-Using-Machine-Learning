import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load model and scaler
model = pickle.load(open("parkinsons_model.sav", "rb"))
scaler = pickle.load(open("scaler.sav", "rb"))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Read all 22 features from the form
        features = []

        for i in range(1, 23):
            features.append(float(request.form[f"f{i}"]))

        # Convert to numpy array
        np_data = np.asarray(features).reshape(1, -1)

        # Scale the input
        np_data = scaler.transform(np_data)

        # Predict
        prediction = model.predict(np_data)

        if prediction[0] == 1:
            output = "⚠️ This person has Parkinson's Disease."
            color = "danger"
        else:
            output = "✅ This person does not have Parkinson's Disease."
            color = "success"

        return render_template(
            "index.html",
            message=output,
            color=color
        )

    except Exception as e:
        return render_template(
            "index.html",
            message=f"Error: {e}",
            color="warning"
        )


if __name__ == "__main__":
    app.run(debug=True)