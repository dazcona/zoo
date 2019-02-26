# Create API of ML model using flask

'''
This code takes the JSON data while POST request an performs the prediction using loaded model and returns
the results in JSON format.
'''

# Import libraries
import numpy as np
import pandas as pd
from sklearn.externals import joblib
from flask import Flask, request, jsonify

app = Flask(__name__)

# Load the model
model = joblib.load('models/zoo.joblib')

@app.route('/api', methods=['POST'])
def predict():

    # Get the data from the POST request
    data = request.get_json(force=True)
    values = list(data.values())

    # Make prediction using model loaded from disk as per the data
    prediction = model.predict([ np.array(values) ])
    # print('Prediction: {}'.format(prediction))

    # Take the first value of prediction
    output = prediction[0]

    return jsonify({ "Prediction": int(output) })

if __name__ == '__main__':
    app.run(port=5000, debug=True)