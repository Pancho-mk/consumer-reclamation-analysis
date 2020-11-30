#!/usr/bin/env python 
# General comparison between country Life e-shop and grizly.cz
import requests
from bs4 import BeautifulSoup

# url from Country Life review and grizly.cz
url = 'https://obchody.heureka.cz/countrylife-cz/recenze/negativni#filtr'
#url = 'https://obchody.heureka.cz/grizly-cz/recenze/negativni#filtr'

headers ={'user-agent': 'Mozilla/5.0 (Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0'}

r = requests.get(url, headers=headers)
print(r.status_code)

print('Working...')

soup = BeautifulSoup(r.text, "lxml") 

# finding total positive and negative
container = soup.find('div', class_='l-shop-detail__navigation')
#print(container)
reviews = container.find('ul', class_='c-subtabs__list')
#print(reviews)
plus_minus = reviews.find_all('li', class_='c-subtabs__item')
for element in plus_minus:
	link = element.a
	number = link['data-count']
	text = element.a.text.strip()
	print(text)
	print(number)

# finding general recomendation
recomendation = soup.find('div', class_='l-shop-detail__wrapper')
percentage = recomendation.find('p', class_='c-shop-detail-recommendation__content').text
print(percentage.strip())

# table info
table_com = soup.find('table', class_='c-shop-detail-stats__table c-stats-table c-stats-table--positive')

tr = table_com.find_all(['tr'])

for elements in tr:
	print(elements.text.strip())
