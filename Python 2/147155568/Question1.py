#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 11:38:44 2022

@author: riddhi
"""

#Installing Packages and defining path
pip install spacy
pip install spacytextblob
import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
nlp = spacy.load("en_core_web_sm") 
nlp.add_pipe('spacytextblob');

allfiles = ['3June2022.txt', '6May2022.txt', '8April2022.txt', '10June2022.txt', '13May2022.txt', '17June2022.txt',
           '20May2022.txt', '24June2022.txt', '27May2022.txt', '29April2022.txt']
path = '/Users/riddhi/Documents/GitHub/homework-3-riddhi-ka-1/'

#Defining the read function to read articles

def read_func(file_name):
        file_path = path + file_name
        f = open(file_path, mode = 'r+t')
        content = f.read()
        return content
        
        
# Reading the articles
content_3June = read_func('3June2022.txt')
content_6May = read_func('6May2022.txt')
content_13May = read_func('13May2022.txt')
content_20May = read_func('20May2022.txt')
content_27May = read_func('27May2022.txt')
content_8April = read_func('8April2022.txt')
content_29April = read_func('29April2022.txt')
content_10June = read_func('10June2022.txt')
content_24June = read_func('24June2022.txt')
content_17June = read_func('17June2022.txt')
content_10June = read_func('10June2022.txt')

#Importing Geonamescashe
import geonamescache

gc = geonamescache.GeonamesCache()

countries = gc.get_countries()

#defining fuction to get the name of countries
def gen_dict_extract(var, key):
    if isinstance(var, dict):
        for k, v in var.items():
            if k == key:
                yield v
            if isinstance(v, (dict, list)):
                yield from gen_dict_extract(v, key)
    elif isinstance(var, list):
        for d in var:
            yield from gen_dict_extract(d, key)
        
countries = [*gen_dict_extract(countries, 'name')]


#3rd June list of Countries

doc_3June = nlp(content_3June)


def get_countries1(doc):
    for ent in doc.ents:
        if ent.label_ == 'GPE':
            if ent.text in countries:
                print(f"Country : {ent.text}")
                

print(get_countries1(doc_3June))
print(get_countries1(doc_10June))
print(get_countries1(doc_17June))
print(get_countries1(doc_24June))
print(get_countries1(doc_8April))
print(get_countries1(doc_29April))
print(get_countries1(doc_6May))
print(get_countries1(doc_13May))
print(get_countries1(doc_20May))
print(get_countries1(doc_27May))
            


#Sentiment Analysis for Polarity
 
SA_3J = doc_3June._.blob.polarity

SA_6M = doc_6May._.blob.polarity

SA_8A = doc_8April._.blob.polarity

SA_10J = doc_10June._.blob.polarity

SA_13M = doc_13May._.blob.polarity

SA_17J = doc_17June._.blob.polarity

SA_20M = doc_20May._.blob.polarity

SA_24J = doc_24June._.blob.polarity

SA_27M = doc_27May._.blob.polarity

SA_29A = doc_29April._.blob.polarity

#Storing the data in the Dataframe
import pandas as pd
  
Polarity_data = [['04-08-2022', SA_8A], ['04-29-2022', SA_29A ], ['05-06-2022', SA_6M], ['05-13-2022', SA_13M], ['05-20-2022', SA_20M],['05-27-2022', SA_27M], ['06-03-2022', SA_3J], ['06-10-2022', SA_10J], ['06-17-2022', SA_17J], ['06-24-2022', SA_24J]]
  
Plot_data = pd.DataFrame(Polarity_data, columns=['Date', 'Polarity'])
print(Plot_data)

#Plotting a bar graph for the Polarity
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
plt.bar(Plot_data['Date'], Plot_data['Polarity'], color = 'Pink')
fig.autofmt_xdate()
ax.set_yticks(np.arange(-0.2, 0.1, 0.1))
ax.set_title('Sentinment Analysis Plot for Polarity')
ax.set_ylabel('Polarity');
ax.set_xlabel('Date of Articles');
plt.savefig('question1 (a)_plot.png')
plt.show()

#Sentiment Analysis for Subjectivity 
S_3J = doc_3June._.blob.subjectivity

S_6M = doc_6May._.blob.subjectivity

S_8A = doc_8April._.subjectivity

S_10J = doc_10June._.subjectivity

S_13M = doc_13May._.blob.subjectivity

S_17J = doc_17June._.blob.subjectivity

S_20M = doc_20May._.blob.subjectivity

S_24J = doc_24June._.blob.subjectivity

S_27M = doc_27May._.blob.subjectivity

S_29A = doc_29April._.blob.subjectivity

#Storing the data in the Dataframe
  
Subjectivity_data = [['04-08-2022', S_8A], ['04-29-2022', S_29A ], ['05-06-2022', S_6M], ['05-13-2022', S_13M], ['05-20-2022', S_20M],['05-27-2022', S_27M], ['06-03-2022', S_3J], ['06-10-2022', S_10J], ['06-17-2022', S_17J], ['06-24-2022', S_24J]]
  
Plot_data1 = pd.DataFrame(Subjectivity_data, columns=['Date', 'Subjectivity'])
print(Plot_data1)

#Plotting a bar graph for the Polarity

fig, ax = plt.subplots()
plt.bar(Plot_data1['Date'], Plot_data1['Subjectivity'], color = 'green')
fig.autofmt_xdate()
ax.set_title('Sentinment Analysis Plot for Subjectivity')
ax.set_ylabel('Subjectivity');
ax.set_xlabel('Date of Articles');
plt.savefig('question1 (b)_plot.png')
plt.show()


