from flask import Blueprint,request
import json
from pipeline.location_pipeline import location_prediction

location = Blueprint('location', __name__)

@location.route('/location', methods=['POST'])
def location_1():
    location_details = request.json
    print(location_details)
    output = location_prediction(location_details)
    json_output = json.dumps(output)
    print(json_output)
    return json_output
