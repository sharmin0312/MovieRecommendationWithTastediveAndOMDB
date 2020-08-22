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
   
def get_sorted_recommendations(lst):
    new_list = get_related_titles(lst)
    new_dict = {}
    for i in new_list:
        rating = get_movie_rating(get_movie_data(i))
        new_dict[i] = rating
    print(new_dict)
    #print(sorted(new_dict, reverse=True))
    return [i[0] for i in sorted(new_dict.items(), key=lambda item: (item[1], item[0]), reverse=True)]

    
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
# get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])

