import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge

app = Flask(__name__)

# Load the scaler and model
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('ridge.pkl', 'rb') as f:
    model = pickle.load(f)

# Route for homepage
@app.route('/')
def home():
    return render_template('index.html')

# Route for prediction
@app.route('/predict_data/', methods=['POST', 'GET'])
def predict_datapoint():
    if request.method == 'POST':
        try:
            # Get the form data
            features = [float(x) for x in request.form.values()]
            # Transform the input using the scaler
            scaled_features = scaler.transform([features])
            # Make prediction using the model
            prediction = model.predict(scaled_features)
            # Prepare response
            return render_template('result.html', prediction=prediction)
        except Exception as e:
            return jsonify({'error': str(e)})
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
