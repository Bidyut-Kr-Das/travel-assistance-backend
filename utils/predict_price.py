import pickle
import pandas as pd

with open("./models/price_prediction_model.pkl", "rb") as f:
    price_model = pickle.load(f)

def time_to_category(time):
    time = int(time.split(':')[0])
    if time < 6 and time >= 3:
        return 1
    elif time < 12 and time >= 6:
        return 4
    elif time < 18 and time >= 12:
        return 0
    elif time < 21 and time >= 18:
        return 2
    elif time< 24 and time >= 21:
        return 5
    else:
        return 3
    
def class_to_category(cls):
    if cls == 'Economy':
        return 1
    else:
        return 0
    
def stops_to_category(stops):
    if stops == "zero":
        return 2
    elif stops == "one":
        return 0
    else:
        return 1

def prepare_data(flight_data):
    # Convert raw dict to dataframe
    df = pd.DataFrame(flight_data, index=[0])

    # create departure time col from time
    df["departure_time"] = df['time'].apply(time_to_category)

    # encode the class column
    df["class"] = df['class'].apply(class_to_category)

    # encode the stops column
    df["stops"] = df['stops'].apply(stops_to_category)

    # encode the source, destination and airline column
    df = pd.get_dummies(df, columns=["source_city", "destination_city", "airline"])

    #drop the time and date column
    df.drop(columns=["date", "time"], inplace=True)

    #change the encoded col from boolean to int
    for col in df.columns:
        if df[col].dtype == "bool":
            df[col] = df[col].astype(int)
    
    # add missing columns from the model feature names
    for col in price_model.feature_names_in_:
        if col not in df.columns:
            df[col] = 0
    #reorder the column names according to model
    df = df[price_model.feature_names_in_]

    return df
    


def predict_price(flight_data):
    processed_data = prepare_data(flight_data)
    return price_model.predict(processed_data)