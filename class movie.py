
"""
Created on Wed May 22 22:49:51 2019
compile movie data into a dictionary object
@author: Miner
"""
import os
import json
import requests
class MovieData:
    
    def __init__(self,movie_title):
        
        self.title = movie_title
        os.chdir(r'C:\Users\Miner\Desktop\movie_website')
        if os.path.isfile(movie_title +"_json.txt") == False:
            params = {'t':movie_title}#, "apikey":'cb44598d'}
            response = requests.get('http://www.omdbapi.com/?', params)
            movie_url = response.url
            movie_data = response.text
            self.movie_json = json.loads(movie_data)
            with open(movie_title +"_json.txt", "w") as file:
                for line in movie_data:
                    os.chdir(r'C:\Users\Miner\Desktop\movie_website')
                    file.write(line)
                    
                print("json text saved to file")
        else:
            print("json file already exits")
            os.chdir(r'C:\Users\Miner\Desktop\movie_website')
            file = open(movie_title +"_json.txt", "r")
            movie_data = file.read()
            self.movie_json = json.loads(movie_data)

movies=["boomerang","boyz n the hood","poetic justice","the patriot","jerry maguire","top gun"]
for movie in movies:
    data=MovieData(movie)
            
            
            

        


        

            

    
        
        
    
 
        
        
   
    
    
    
    


        
        

