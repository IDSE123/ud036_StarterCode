import media
import fresh_tomatoes
import webbrowser
import httplib
import json

border = media.Movie("Border", "Story of Ind pak", "https://upload.wikimedia.org/wikipedia/en/9/9c/Border1997.jpg", "https://www.youtube.com/watch?v=pjxhnco4J5A") #creating first instance of class Movie 

#Just to confirm if the class file has been imported succesfully
    #print border.title
    #webbrowser.open(border.trailer)
gadar = media.Movie("Gadar", "Story of Ind Pak partition", "https://upload.wikimedia.org/wikipedia/en/6/67/Gadar.jpg", "https://www.youtube.com/watch?v=2BeLl3qdNlo")
loc = media.Movie("LOC", "Story of Kargil war", "https://upload.wikimedia.org/wikipedia/en/f/fd/Loc_poster.jpg", "https://www.youtube.com/results?search_query=LOC")
tango = media.Movie("Tango Charlie", "Story of BSF soldiers", "https://upload.wikimedia.org/wikipedia/en/5/5a/Tango_charlie.jpg", "https://www.youtube.com/watch?v=S4cgOZGNsk0")

#an array of movies to send all the above objects as argument to open_movies_page function
movies = [border, gadar, loc, tango]


#Calling the function open_movies_page from fresh_tomatoes.py which will create the webpage
fresh_tomatoes.open_movies_page(movies, "normal")


