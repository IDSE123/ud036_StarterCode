import media
import fresh_tomatoes
import webbrowser
import httplib
import json


#conn object to connect to the api
conn = httplib.HTTPSConnection("api.themoviedb.org")
payload = "{}"
conn.request("GET", "/3/discover/movie?page=1&include_video=true&include_adult=true&sort_by=popularity.desc&language=en-US&api_key=ac05a8d8bd9776dfc277e908c1aaeb2d", payload)
res = conn.getresponse()
data = res.read()

#print(data.decode("utf-8"))
json_object = json.loads(data)

#title
#title_from_json = json_object["results"][0]["title"]

#description
#description_from_json = json_object["results"][0]["overview"]


#poster_json = "https://image.tmdb.org/t/p/w500/"+json_object["results"][0]["poster_path"]
#webbrowser.open(youtube_key)

i = 0 # loop iterator
my_list = [] # array to store all the instances of the top 5 movies fetched freom the api
while i<5:
    #to get the trailer we have to get the youtube key
    conn2 = httplib.HTTPSConnection("api.themoviedb.org")
    payload2 = "{}"
    movie_id = json_object["results"][i]["id"]
    conn2.request("GET", "/3/movie/"+str(movie_id)+"/videos?language=en-US&api_key=ac05a8d8bd9776dfc277e908c1aaeb2d", payload2)
    res2 = conn2.getresponse()
    data2 = res2.read()
    json_object2 = json.loads(data2)
    
    #youtube_key
    youtube_key = "https://www.youtube.com/watch?v="+json_object2["results"][0]["key"]
    poster_json = "https://image.tmdb.org/t/p/w500/"+json_object["results"][i]["poster_path"]
    my_list.append(media.Movie(json_object["results"][i]["title"], json_object["results"][i]["overview"], poster_json, youtube_key))
    i = i + 1

#finally calling the open_movies_page function to make the webpage
fresh_tomatoes.open_movies_page(my_list, "api")
