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

def extract_movie_titles(dic):
    return ([i['Name'] for i in dic['Similar']['Results']])

def get_related_titles(movie_list):
    li = []
    for movie in movie_list:
        li.extend(extract_movie_titles(get_movies_from_tastedive(movie)))
    return list(set(li))        
    
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_related_titles(["Black Panther", "Captain Marvel"])
# get_related_titles([])

