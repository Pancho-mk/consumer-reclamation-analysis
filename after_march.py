#!/usr/bin/env python 
# the response after March 2020
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

lst_after = [('2020-'+'0'+str(y)) if (len(str(y)) == 1) else ('2020-'+str(y)) for y in range(4, 12)]

numpy_array = []
#how many after march 2020 reclamations?
for x in lst_after:
	filt2 = df['Datum'].str.contains(x, na=False)
	reclamation_march_2020 = df[filt2].Datum.count()
	print(f'Total  complaints for {x}: {reclamation_march_2020}')
	#df to txt
	numpy_array.append(df[filt2].to_numpy())

np.savetxt("after_march_2020.txt", numpy_array, fmt = "%s")

for x in lst_after:
	# filtering df column that has 2020 in Datum AND has a answer(Odpoved)
	filt = (df['Datum'].str.contains(x, na=False) ) & (df['Odpoved'] == df['Odpoved'])
	# show those columns that fulfil both the condition: (only filt returns True/False)
	#how many answered complaints
	answers_march_2020 = df[filt].Datum.count()
	#print(answers_2020)
	print(f'Total response for {x}: {answers_march_2020}')

File_object = open(r"after_march_2020.txt","r")
f = File_object.read()
most_common_words = count_words_fast(f)

print(most_common_words.most_common(100))

