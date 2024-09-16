from flask import Blueprint,request
import json

#function import 
from pipeline.flight_pipeline import flight_prediction


prediction = Blueprint('prediction', __name__)

@prediction.route('/predict', methods=['POST'])
def predict():
    data = request.json # <- data is dictionary
    output = flight_prediction(data)
    json_output = json.dumps(output)
    return json_output