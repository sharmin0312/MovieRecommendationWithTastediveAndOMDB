import requests_with_caching
import json


def get_movie_data(s):
    endpoint = 'http://www.omdbapi.com/'
    param = {}
    param['t'] = s
    param['r'] = 'json'
    res = requests_with_caching.get(endpoint, params=param)

    return res.json()
print(get_movie_data("Deadpool 2"))

def get_movie_rating(dic):
    rate = dic['Ratings']
    for dic_item in rate:
        if dic_item['Source'] == 'Rotten Tomatoes':
            return int(dic_item['Value'][:-1])
    return 0
   
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movie_rating(get_movie_data("Deadpool 2"))

