# -*- coding: utf-8 -*-
"""
Generate movie json file from OMDB API
Created on Tue May 21 18:31:28 2019
@author: Miner
"""
import os
import json
import requests


def get_movie_json(movie_title):
    if os.path.isfile(movie_title +"_json.txt") == False:
        params = {'t':movie_title}
        response = requests.get('http://www.omdbapi.com/?', params)
        movie_url = response.url
        movie_data = response.text
        movie_json = json.loads(movie_data)
        with open(movie_title +"_json.txt", "w") as file:
            for line in movie_data:
                file.write(line)
            print("json text saved to file")
            return movie_json
    print("json file already exits")
    file = open(movie_title +"_json.txt", "r")
    try:
        file_text = file.read()
        movie_json = json.loads(file_text)
        return movie_json

    except:
        print("returning file didn't work")

    file.close()

#top_gun_data = get_movie_json('top gun')



