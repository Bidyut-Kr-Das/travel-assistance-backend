from flask import Flask
from flask_cors import CORS
#importing routes
from routes.prediction_route import prediction
from routes.city_route import cities
from routes.location_route import location


app = Flask(__name__)
CORS(app, supports_credentials=True, resources={r"/api/*": {"origins": "*"}})

app.register_blueprint(prediction,url_prefix='/api/v1')

app.register_blueprint(cities,url_prefix='/api/v1')

app.register_blueprint(location,url_prefix='/api/v1')


if __name__ == '__main__':
    app.run(debug=True,host="192.168.2.123",port=8080)


