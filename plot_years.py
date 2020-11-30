#!/usr/bin/env python 
# Ploting the results from Complaints over the years
# for Country Life in Heureka.cz
# Python 3.6
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt

# Access years in df
df = pd.read_csv('countrylife.csv')
date = df['Datum'].tolist()

date2 = [s.split(' ')[0] for s in date]
 # transfer df to a list
years = [s.split('-')[0] for s in date2]
#days = [s.split('-')[2] for s in clean_data_list]
#print(years)

# Count the years
c = Counter(years)
print(c)

# preserve the order from the counter object(which is as dict)
ordered_lst = c.most_common()  # to a list of tuples
print('ordl:', ordered_lst)

#unpacking the list of tuples into 2 seperate lists
year_bar = []
frequency_bar = []

for item in ordered_lst:
	year_bar.append(item[0])
	frequency_bar.append(item[1])

#ploting the results in a ordered way
frequency_bar, year_bar = zip(*sorted(zip(frequency_bar, year_bar), reverse=True))
print(year_bar)
print(frequency_bar)


total_compl = sum(frequency_bar)
years_num = len(year_bar)
average_per_year = total_compl / years_num
print('Average per year:', average_per_year)
average_per_month = average_per_year / 12
print('Average per month:', average_per_month)

#Ploting the results
plt.bar(year_bar, frequency_bar, label= "Reclamation", color= "green", alpha=.6)
# x-axis label 
plt.xlabel("Years\n  source:  https://obchody.heureka.cz/countrylife-cz/recenze/negativni#filtr")
#plt.xlabel('https://obchody.heureka.cz/countrylife-cz/recenze/negativni#filtr')
# frequency label 
plt.ylabel('Reclamation')
# plot title 
plt.title('Reclamation on Heureka.cz')
# showing legend 
plt.legend()
# function to show the plot 
plt.show()
