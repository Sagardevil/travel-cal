from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd
import os
from model.preprocessing import preprocess_input

app = Flask(__name__)

# Load the model
model_path = os.path.join('model', 'travel_income_model.pickle')
with open(model_path, 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        data = request.form.to_dict()
        
        # Preprocess the input
        features = preprocess_input(data)
        
        # Make prediction
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features).max()
        
        return jsonify({
            'prediction': prediction,
            'probability': round(probability * 100, 2)
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)