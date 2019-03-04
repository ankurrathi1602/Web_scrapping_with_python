#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 00:41:05 2019

@author: ankurrathi
"""
def movies_name():
    from bs4 import BeautifulSoup
    import requests
    
    req = requests.get('https://www.imdb.com/list/ls009454990/')
    
    soup = BeautifulSoup(req.text, 'lxml')
    
    movie = soup.find('div', {'class':'lister'})
    
    movie1 = movie.find_all('h3', {'class':'lister-item-header'})
    
    for count,m in enumerate(movie1, 1):
        h3 = m.find('a')
        print(count, h3.text)

movies_name()