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

@app.route('/')
def accept_cert():
    # Set a cookie with Secure and SameSite=None attributes
    response = make_response(redirect('https://dynamic-travel-assistant.vercel.app/services'))
    response.set_cookie('sslAccepted', 'true', max_age=60*60*24*10, secure=True, samesite='None')
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", ssl_context=('cert.pem', 'key.pem'))


