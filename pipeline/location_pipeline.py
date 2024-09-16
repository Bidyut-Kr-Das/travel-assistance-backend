import requests
from controllers.location_fetch import fetch_coords

def location_prediction(location_details):
    # 1. Access the source_city from the location details
    airport_code = location_details["airport_code"]

    # 2. find the airport closest to the source city and Fetch the lat and long of the airport from that data
    airport_list = fetch_coords(airport_code)
    
    # 4. Access the location of the user from the location details
    latitude_user = location_details["latitude"]
    longitude_user = location_details["longitude"]

    # 5. Calculate the distance between the user location and the airport location
    latitude_airport = airport_list["latitude_deg"]
    longitude_airport = airport_list["longitude_deg"]
    
    # 6. Return the distance and time to reach the airport
    url = f"https://api.distancematrix.ai/maps/api/distancematrix/json?origins={latitude_user},{longitude_user}&destinations={latitude_airport},{longitude_airport}&key=8Dlht1PwB6mikJNr1qKaMtyg2lgHUJTqm9KWce4c9MszyGq5jqJRUOdHFHinnjGW"
    
    response = requests.get(url)

    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Extract the distance and duration
        distance = data['rows'][0]['elements'][0]['distance']['text']
        duration = data['rows'][0]['elements'][0]['duration']['text']
    
    output = {
        "airport_name": airport_list["name"],
        "distance": distance,
        "duration": duration,
        "mode_of_transport": "car"
    }
    return output
