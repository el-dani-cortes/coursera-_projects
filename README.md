# Coursera courses

Designing RESTful APIs

## Make Your Own API Mashup

Retrive main information of the first restaurant in that send the Foursquare API using a location and a meal type.

## Requirements

* Have an account on the google map API:
    https://developers.google.com/maps/?hl=en
* Have an account on the Foursquare developer webpage:
    https://developer.foursquare.com/
* Python 3 version


## Usage

1. Clone the repo:
```
$ git clone https://github.com/el-dani-cortes/coursera_projects.git
```
2. Create a virtual enviroment:
```
$ source venv/bin/activate ./venv
```

3. Install requirements dependencies from requirements.txt file:
```
$ pip install -r requirements.txt
```

4. Create a file `.env` in the same directory path of your project and add your credentials values of the APIs:
```
.env

# Google developer's credentials
GOOGLE_API_KEY='xxx'

# Foursquare developer's credentials
CLIENT_ID='xxx'
CLIENT_SECRET='xxx'
```
5. Finally run the program:
```
$ python3 findARestaurant.py
```


