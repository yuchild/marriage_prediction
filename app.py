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
    age = model.predict([[int(request.args['gender'])
                          , int(request.args['caste'])
                          , int(request.args['religion'])
                          , int(request.args['mother_tongue'])
                          , int(request.args['country'])
                          , int(request.args['height_cms'])
                         ]])
    # in url: 
    # http://127.0.0.1:5000/predict? \ 
    # gender=1&caste=2&religion=2&mother_tongue=5 \ 
    # &country=5&height_cms=175
    
    return str(age)

app.run(debug=True)