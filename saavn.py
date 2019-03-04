#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 23:26:26 2019

@author: ankurrathi
"""

from bs4 import BeautifulSoup
import requests

res = requests.get('https://www.jiosaavn.com/featured/weekly-top-songs/8MT-LQlP35c_')

soup = BeautifulSoup(res.text, 'lxml')

data = soup.find('ol', {'class':'content-list'})
all_songs = data.find_all('div', {'class':'details'})
for count,s in enumerate(all_songs, 1):
    song = s.find('p', {'class':'song-name'})
    print(count, song.text)