import flask
from flask import request
app = flask.Flask(__name__)

from flask_cors import CORS
CORS(app)

@app.route('/')
def home():
    return '<h1>The API Server is working!</h1>'

@app.route('/predict')
def predcit():
    import joblib
    model = joblib.load('marriage_age_prediction_model.ml')
    age = model.predict([[1, 2, 5, 6, 5, 175]])
    return str(age)

app.run(debug=True)