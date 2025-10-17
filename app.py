from flask import Flask, request, render_template
import numpy as np
from tensorflow.keras.models import load_model
import joblib

app = Flask(__name__)

# Load model and scaler
model = load_model("fraud_model.h5")
scaler = joblib.load("scaler.joblib")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Read all form input values
        input_data = [float(x) for x in request.form.values()]
        input_data = np.array(input_data).reshape(1, -1)
        input_scaled = scaler.transform(input_data)

        # Predict
        prediction = model.predict(input_scaled)
        prob = float(prediction[0][0])
        result = "Fraudulent" if prob > 0.5 else "Legitimate"

        return render_template(
            'index.html',
            prediction_text=f"Prediction: {result} (Probability: {prob:.4f})"
        )
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {e}")

if __name__ == '__main__':
    app.run(debug=True)
