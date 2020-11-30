#!/usr/bin/env python 
# Ploting how many time CL answered to those complains in total/over the years
#python3.6
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt
from collections import OrderedDict

# Access answers in df
df = pd.read_csv('countrylife.csv')
answers_column = df['Odpoved'].tolist()
answers = [x for x in answers_column if x == x]   #answered = not nan values


print(f'Total complaints: {len(answers_column)}')
print(f'Total answered complaints: {len(answers)}')
#print(answers)

# calculate percentage of total response
response2 = (len(answers) / len(answers_column)) * 100
response = round(response2)
print(f'Total response: {response} %')

# answers per 2020
# total 2020
# filtering df column that has 2020 in Datum AND has a answer(Odpoved)
filt = (df['Datum'].str.contains('2020', na=False) ) & (df['Odpoved'] == df['Odpoved'])
# show those columns that fulfil both the condition: (only filt returns True/False)

#how many 2020 reclamations?
filt2 = df['Datum'].str.contains('2020', na=False)
reclamation_2020 = df[filt2].Datum.count()
print(f'Total  complaints for 2020: {reclamation_2020}')

#how many answered complaints
answers_2020 = df[filt].Datum.count()
#print(answers_2020)
print(f'Total response for 2020: {answers_2020}')

#Percentage
perc = (answers_2020 / reclamation_2020) * 100
print(f'Percentage of answered complaints in 2020: {round(perc)} %')



# answers per year
date = df['Datum'].tolist()

date2 = [s.split(' ')[0] for s in date]
 # transfer df to a list
years = [s.split('-')[0] for s in date2]

years_unique = sorted(list(set(years)))
print(years_unique)

# traverse in df to receive 3 lists for reclamation/answer/percentage
answers_x = []
reclamation_x = []
perc_x = []
for x in years_unique:
	filt = (df['Datum'].str.contains(x, na=False) ) & (df['Odpoved'] == df['Odpoved'])
	a_x = df[filt].Datum.count()
	answers_x.append(a_x)

	filt2 = df['Datum'].str.contains(x, na=False)
	r_x = df[filt2].Datum.count()
	reclamation_x.append(r_x)

	p_x = round((a_x / r_x) * 100)
	perc_x.append(p_x)


print(answers_x)
print(reclamation_x)
print(perc_x)

# Print year/reclamation/answer
dict1 = OrderedDict(zip(years_unique, reclamation_x))
print(dict1)
dict2 = OrderedDict(zip(years_unique, answers_x))
print(dict2)
dict3 = OrderedDict((k, f'{dict1[k]}, {dict2[k]}') for k in dict1 if k in dict2)
print(dict3)


plt.bar(years_unique, perc_x, label= "percentage", color= "green", alpha=.7)
# x-axis label 
plt.xlabel("Complaints/answers per year: ('2010', '1, 0'), ('2011', '4, 3'), ('2012', '4, 1'), ('2013', '10, 0'),\n ('2014', '8, 1'), ('2015', '8, 4'), ('2016', '5, 4'), ('2017', '4, 4'), ('2018', '1, 1'),('2019', '3, 2'),('2020', '37, 26')", fontsize=7.5, fontweight='bold')
#plt.xlabel('https://obchody.heureka.cz/countrylife-cz/recenze/negativni#filtr')
# frequency label 
plt.ylabel('Percentage')
# plot title 
plt.title('Percentage for answers/reclamation over the years on Heureka.cz')
# showing legend 
plt.legend()
# function to show the plot 
plt.show()
