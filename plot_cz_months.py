import numpy
import requests
import pandas as pd
from bs4 import BeautifulSoup 
from collections import Counter
from matplotlib import pyplot as plt

def ord_months_names(ord_lst, l_months):
	'''ord_list: ordered list of numbers 1-12, unique, 12 elements
	 l_months: list of numbers representing months 1-12, unique, 12 elements
	Returns ord_final:ordered list of months by name(coresponding to the order 
	of the numbers in the provided ord_list
	'''
	# Providing a list of numbers from 1-12 to corespond with the months
	t_1 = [str(x) for x in range(1, 13)]   
	t = ['0'+ x if len(x) == 1 else x for x in t_1] #adding leading zero if number is 1 number
	#print('t:', t)
	z = zip(t, l_months) 
	d = dict(z)
	#print('d:', d)
	# list comprehension:
	# while traversing the list check if the element is present 
	# and if it is take the corespondent value and put it into a list
	ord_final = [d[element] for element in months_bar if element in d]
	print('2:', ord_final)
	return ord_final
 
def lst_from_s(t):
 	# return list from string 
 	# with individual elements
	return t.split(',') 

def cz_months():
	# returns the czech moths scrubed from Wikipoedia
	r_cz = requests.get('https://en.wikiversity.org/wiki/Czech_Language/Months_and_Dates')
	soup_cz = BeautifulSoup(r_cz.text, 'lxml')
	cont = soup_cz.find('div', class_='mw-parser-output')
	table_com = soup_cz.find('table', class_='wikitable')
	#table_com2 = table_com[0]
	table_rows = table_com.find_all(['tr'])

	results = []
	for tr in table_rows:
	    td = tr.find_all('td')
	    row = [i.text for i in td]
	    #print(row)
	    results.append(row)

	#print(results)
	lst_cz = []
	month_cz = results[2:14]
	for element in results:
		try:
			month = element[1].strip()
			lst_cz.append(month)
		except Exception:
			None

	return lst_cz


df = pd.read_csv('countrylife.csv')
date_list = df['Datum'].tolist()      # transfer df to a list

#clean the hours from the date-time provided by pandas
clean_data_list = [s.split(' ')[0] for s in date_list]
months = [s.split('-')[1] for s in clean_data_list]
days = [s.split('-')[2] for s in clean_data_list]

# print(months)
# print(days)
#count how many complaints/month from the list
count = Counter(months)
count['11'] = 0                # adding value for November because it does not exist
#print(count)

# preserve the order from the counter object(as dict)
ordered_dict = count.most_common()  # list of tuples
#print('ordic:', ordered_dict)

#unziping the dictonary into 2 seperate lists
months_bar = []
frequency_bar = []

for item in ordered_dict:
	months_bar.append(item[0])
	frequency_bar.append(item[1])

''' because the original date format from a web scraping 
is with leading '0' in single numbered months and 
range provided list of numbers without '0', we have to 
make it in the same format in order the dictionary could
be recognized as equal in the function ord_l
'''
months_bar9 = ['0'+ x if len(x) == 1 else x for x in months_bar]

#ploting the results in a ordered way
frequency_bar, months_bar = zip(*sorted(zip(frequency_bar, months_bar9), reverse=True))
# months_bar = count.keys()
# frequency_bar = count.values()

# Making list of months from a string of months grabed from the internet
s = 'January, February, March, April, May, June, July, August, September, October, November, December'
months_list = lst_from_s(s)
# Calling a function to receive ordered list of months
months_bar_names = ord_months_names(list(months_bar), months_list)

# In Czech language
months_list_cz = cz_months()  #returns list of czech months
#months_list_cz = lst_from_s(k)
# Calling a function to receive ordered list of months in Czech language
print('months_bar:', months_bar)
print('months_list_cz:', months_list_cz)
months_bar_names_cz = ord_months_names(list(months_bar), months_list_cz)

c = range(len(frequency_bar))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.bar(c, frequency_bar)

plt.xticks(c, months_bar_names_cz)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)

plt.title("Reklamace na Heureka.cz")
plt.xlabel("Měsíce\n  zdroj:  https://obchody.heureka.cz/countrylife-cz/recenze/negativni#filtr")
plt.ylabel("Celkový počet stížností")

plt.show()