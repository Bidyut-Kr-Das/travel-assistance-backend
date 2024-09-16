from utils.predict_price import predict_price
from utils.predict_delay import predict_delay
from controllers.flight_data_fetch import get_flight_data


def flight_prediction(user_data):

    output = {} #<- dictionary to store the output of each step

    # 1. Predict the price of the flight from user data
    predicted_price = predict_price(user_data)
    output["predicted_price"] = round(predicted_price[0],2)

    # 2. Fetch top 3 flight data from the database closest to the predicted price
    top_3_flights = get_flight_data(user_data, output["predicted_price"])
    output["flights"] = top_3_flights

    # 3. Predict the average delay for the flights
    predicted_delay = predict_delay(user_data)
    output["predicted_delay"] = round(predicted_delay[0],0)

    return output