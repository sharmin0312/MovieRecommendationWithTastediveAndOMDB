import json
import requests_with_caching

def get_movies_from_tastedive(s):
    baseurl="https://tastedive.com/api/similar"
    para={}
    para['q']=s
    para['type']='movies'
    para['limit']=5
    res=requests_with_caching.get(baseurl,params=para)
    return res.json()

# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_movies_from_tastedive("Bridesmaids")
# get_movies_from_tastedive("Black Panther")

