import requests
import json
"""get movie info from omdb"""



#search paramaters in form of a dict 't'= movie title
#d = {'t': 'office space'} 
input("Enter movie)

d = {'t': 'office space','apikey': 'cb44598d'}

#get request
response = requests.get('http://www.omdbapi.com/?', params=d) 

#search url
movie_url = response.url 

#text from website in the form of a string                                     
movie_data = response_obj.text

#save movie_data string to a file
with open('office space.txt','w') as file:
    for line in movie_data:
        file.write(line)

#coverts movie_data string to json(dictionary)
movie_json = json.loads(movie_data)


        
        
    