import requests
from dotenv import dotenv_values

# Get enviroment variables
config = dotenv_values(".env")

def getGeocodeLocation(inputString):    
    """
    Get latitude and longitude coordinates of a place using the google map's API
    
    :param inputString: Strung with the place to search
    :return: A tuple with latitude and longitude 
    """
    # Use Google Maps to convert a location into Latitute/Longitute coordinates
    # FORMAT: https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=API_KEY
    GOOGLE_AIPI_KEY = config["GOOGLE_API_KEY"]
    locationString = inputString.replace(" ", "+")
    url = (f'https://maps.googleapis.com/maps/api/geocode/json?address={locationString}&key={GOOGLE_AIPI_KEY}')
    try:
        r = requests.get(url)
        results = r.json()["results"][0]
        latitude = results["geometry"]["location"]["lat"]
        longitude = results["geometry"]["location"]["lng"]
    except requests.HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    except Exception as err:
        print(f'Other error occurred: {err}')
    return(latitude,longitude)


if __name__ == '__main__':
    #This is a example for Dala, Texas.
    getGeocodeLocation("dallas texas")