#!/usr/bin/env python 
#python 3.6
# Consumer analysis for complains for Country Life cz e-shop on Heureka.cz
import requests
from bs4 import BeautifulSoup
import csv
import time

# Scraping for the result on heureka.cz/ seting the list of url's for all the result
url_list = ['https://obchody.heureka.cz/countrylife-cz/recenze/negativni#filtr']
i = 2
while i < 6:
	url_join = 'https://obchody.heureka.cz/countrylife-cz/recenze/negativni?f='+str(i)+'#filtr'
	url_list.append(url_join)
	i += 1

#set csv writer - writing the result in csv file
csv_file = open('countrylife.csv', 'w')
csv_writer = csv.writer(csv_file)   
csv_writer.writerow(['Datum', 'Author', 'Attributes', 'Recenze', 'Odpoved'])

for url in url_list:
	print('Working...')

	headers ={'user-agent': 'Mozilla/5.0 (Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0'}

	r = requests.get(url, headers=headers)
	time.sleep(10)

	print(r.status_code)

	soup = BeautifulSoup(r.text, "lxml") 

	container = soup.find('div', class_='c-pagination js-pagination')
	recenze_block = container.find_all('li', class_='c-box-list__item c-post')
	for recenze in recenze_block:
		datum_cz = recenze.find('time', class_='c-post__publish-time').text
		datum_format = recenze.time.get('datetime')
		author = recenze.find('div', class_='c-post__basic-info o-block-list o-block-list--snug').p.text

		attributes = recenze.find_all('li', class_='c-attributes-list__item')
		try:
			atribute_list = []
			for atribute in attributes:
				#print(atribute.text)
				atribute_list.append(atribute.text)
				#print(atribute_list)
		except Exception as e:
			attributes = None

		try:
			recenze_text = recenze.find('p', class_='c-post__summary').text
		except Exception as e:
			recenze_text = None

		try:
			odpoved = recenze.find('div', class_='c-post__response c-accordion js-accordion js-review-actions is-active').p.text
			#print(odpoved)
		except Exception as e:
			odpoved = None

		#transfering atribute_list into string
		delimiter = '. '
		atribute_text = delimiter.join(atribute_list)

		csv_writer.writerow([datum_format, author, atribute_text, recenze_text, odpoved])

csv_file.close()