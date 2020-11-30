from matplotlib import pyplot as plt
import pandas as pd
from collections import Counter
import numpy
import requests

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

	z = zip(t, months_list) 
	d = dict(z)
	#print('d:', d)

	# list comprehension:
	# while traversing the list check if the element is present 
	# and if it is take the corespondent value and put it into a list
	ord_final = [d[element] for element in months_bar if element in d]
	#print('2:', ord_final)
	return ord_final
 
def lst_from_s(t):
 	# return list from string 
 	# with individual elements
 	return t.split(',') 

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

# preserve the order from the counter object(which is as dict)
ordered_lst = count.most_common()  # to a list of tuples
#print('ordic:', ordered_lst)

#unpacking the list of tuples into 2 seperate lists
months_bar = []
frequency_bar = []

for item in ordered_lst:
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
# print(months_bar)
# print(frequency_bar)

# Making list of months from a string of months grabed from the internet
s = 'January, February, March, April, May, June, July, August, September, October, November, December'
months_list = lst_from_s(s)

#Grabing czech month names
r_cz = requests.get('https://en.wikiversity.org/wiki/Czech_Language/Months_and_Dates')
soup_cz = BeautifulSoup(r_cz.text, 'lxml')
cont = soup_cz.find('div', class_='mw-parser-output')
table_com = soup.find_all('table', class_='wikitable')


months_list_cz = lst_from_s(k)
#print(months_list)

# Calling a function to receive ordered list of months
months_bar_names = ord_months_names(list(months_bar), months_list)

c = range(len(frequency_bar))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.bar(c, frequency_bar)

plt.xticks(c, months_bar_names)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)

plt.title("Complaints in Heureka.cz")
plt.xlabel("Months")
plt.ylabel("Total complaints")

plt.show()