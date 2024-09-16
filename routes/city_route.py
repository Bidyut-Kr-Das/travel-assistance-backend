from flask import Blueprint
import json
from controllers.city_fetch import get_all_cities

cities = Blueprint('cities', __name__)

@cities.route('/cities', methods=['GET'])
def predict():
    cities = get_all_cities()
    json_output = json.dumps({cities: cities})
    return json_output