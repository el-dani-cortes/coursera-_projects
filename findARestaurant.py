#1. Use getGeocodeLocation to get the latitude and longitude coordinates of the location string.

#2.  Use foursquare API to find a nearby restaurant with the latitude, longitude, and mealType strings.
#HINT: format for url will be something like https://api.foursquare.com/v2/venues/search?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=20130815&ll=40.7,-74&query=sushi

#3. Grab the first restaurant
#4. Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
#5. Grab the first image
#6. If no image is available, insert default a image url
#7. Return a dictionary containing the restaurant name, address, and image url

from geocode import getGeocodeLocation
import requests
from dotenv import dotenv_values

# Get enviroment variables
config = dotenv_values(".env")

def findARestaurant(mealType: str, location: str) -> dict:
	"""
    Grab information about restaurants from Foursquare API
    
    :param mealType: Type of food to search
    :param location: String with the place to search
	:return: dictionary containing the restaurant name, address, and image url
    """

	# Keys for Foursquare API
	CLIENT_ID = config["CLIENT_ID"]
	CLIENT_SECRET = config["CLIENT_SECRET"]

	latitude, longitude = getGeocodeLocation(location)
	locationString = str(latitude) + ", " + str(longitude)
	params = dict(
		client_id=CLIENT_ID,
		client_secret=CLIENT_SECRET,
		v='20180323',
		ll=locationString,
		query=mealType,
		limit=1
	)
	try:
		url = 'https://api.foursquare.com/v2/venues/search'
		resp = requests.get(url=url, params=params)
		data = resp.json()
		if data["meta"]["code"] == 200:
			# Grab main info of the first restaurant
			first_restaurant = data["response"]["venues"][0]
			info_restaurant = {}
			info_restaurant["Restaurant name"] = first_restaurant["name"]
			restaurant_address = first_restaurant["location"]["formattedAddress"]
			info_restaurant["Restaurant address"] = " ".join(restaurant_address)

			# Grab image of the restaurant
			restaurant_id = first_restaurant["id"]
			url_photos = f'https://api.foursquare.com/v2/venues/{restaurant_id}/photos'
			params = dict(
				client_id=CLIENT_ID,
				client_secret=CLIENT_SECRET,
				v='20180323',
			)
			resp = requests.get(url=url_photos, params=params)
			photos_data = resp.json()
			if photos_data["meta"]["code"] == 200:
				first_photo = photos_data.get("response").get("photos").get("items")
				if len(first_photo) != 0 or first_photo is not None:
					image_url = first_photo["prefix"] + "300x300" + first_photo["suffix"]
				else:
					image_url = "https://st4.depositphotos.com/14953852/22772/v/600/depositphotos_227725020-stock-illustration-no-image-available-icon-flat.jpg"
				info_restaurant["Image url"] = image_url
			else:
				raise Exception(f'Error type: {photos_data["meta"]["errorType"]}, Code: {photos_data["meta"]["code"]}')
			#Print values of the first restaurant
			for key, value in info_restaurant.items():
				print(f"{key}: {value}")
			print('\n')
		else:
			print(f'Error type: {data["meta"]["errorType"]}, Code: {data["meta"]["code"]}')
	except requests.HTTPError as http_err:
		print(f'HTTP error occurred: {http_err}')
	except Exception as err:
		print(f'Other error occurred: {err}')


if __name__ == '__main__':
	findARestaurant("Pizza", "Tokyo, Japan")
	findARestaurant("Tacos", "Jakarta, Indonesia")
	findARestaurant("Tapas", "Maputo, Mozambique")
	findARestaurant("Falafel", "Cairo, Egypt")
	findARestaurant("Spaghetti", "New Delhi, India")
	findARestaurant("Cappuccino", "Geneva, Switzerland")
	findARestaurant("Sushi", "Los Angeles, California")
	findARestaurant("Steak", "La Paz, Bolivia")
	findARestaurant("Gyros", "Sydney, Australia")
