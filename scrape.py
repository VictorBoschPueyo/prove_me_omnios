## In this file i'll scrape data from web page

import requests
from bs4 import BeautifulSoup
from book import *


url = "http://books.toscrape.com/index.html"
response = requests.get(url)

html = BeautifulSoup(response.text, 'html.parser')

### Get info

########## Get all prices
prices = html.find_all('p', class_="price_color")

prices_list = list()
for p in prices:
    prices_list.append(p.text[2:])

del prices
##########

########## Get all titles and images
info = html.find_all('img')
titles_list = list()
images_list = list()
for i in info:
    images_list.append('http://books.toscrape.com/' + i['src'])
    titles_list.append(i['alt'])

del info
##########

########## Get all star ratings
ratings = html.find_all('p', class_="star-rating")

ratings_list = list()
for r in ratings:
    ratings_list.append(r['class'][1])

del ratings
##########

### Create objects so that everything is in order

library = list()
for b in range(len(images_list)):
    library.append(Book(0, titles_list[b], ratings_list[b], 'pound', float(prices_list[b]), images_list[b]))


del titles_list, ratings_list, prices_list, images_list