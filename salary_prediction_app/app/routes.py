from flask import request, jsonify, render_template
from app import app
import pickle

# Load the trained model
with open('app/model.pkl', 'rb') as file:
    clf = pickle.load(file)


# Default route for home page
@app.route('/')
def home():
    return render_template('index.html')


# Define a route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request form
    experience = float(request.form['experience'])

    # Ensure the input is a 2D array for prediction
    features = [[experience]]

    # Make prediction
    prediction = clf.predict(features)[0]

    # Return the prediction to the UI
    return render_template('index.html', prediction=prediction)
