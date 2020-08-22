
import requests_with_caching
import json


def get_movie_data(s):
    endpoint = 'http://www.omdbapi.com/'
    param = {}
    param['t'] = s
    param['r'] = 'json'
    res = requests_with_caching.get(endpoint, params=param)

    return res.json()

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
print(get_movie_data("Venom"))
# get_movie_data("Baby Mama")

