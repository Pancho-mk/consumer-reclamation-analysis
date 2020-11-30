#!/usr/bin/env python 
# Ploting the response for March 2020, percentage of answered and word count most frequent
# python3.6
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt
from collections import OrderedDict
import numpy as np
from collections import Counter

def count_words_fast(text):	 #counts word frequency using Counter from collections 
	text = text.lower() 
	skips = [".", ", ", ":", ";", "'", '"'] 
	for ch in skips: 
		text = text.replace(ch, "") 
	word_counts = Counter(text.split(" ")) 
	return word_counts 

df = pd.read_csv('countrylife.csv')

#how many march 2020 reclamations?
filt2 = df['Datum'].str.contains('2020-03', na=False)
reclamation_march_2020 = df[filt2].Datum.count()
print(f'Total  complaints for March 2020: {reclamation_march_2020}')

# filtering df column that has 2020 in Datum AND has a answer(Odpoved)
filt = (df['Datum'].str.contains('2020-03', na=False) ) & (df['Odpoved'] == df['Odpoved'])
# show those columns that fulfil both the condition: (only filt returns True/False)
#how many answered complaints
answers_march_2020 = df[filt].Datum.count()
#print(answers_2020)
print(f'Total response for march 2020: {answers_march_2020}')

#Percentage
perc = (answers_march_2020 / reclamation_march_2020) * 100
print(f'Percentage of answered complaints for March 2020: {round(perc)} %')

# df to txt
# numpy_array = df[filt2].to_numpy()
# np.savetxt("march_2020_2.txt", numpy_array, fmt = "%s")

File_object = open(r"march_2020_2.txt","r")
f = File_object.read()
most_common_words = count_words_fast(f)

print(most_common_words.most_common(200))