# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 17:49:50 2022

@author: khadk
"""

import re
import os
import nltk
import spacy
 
# essential entity models downloads
nltk.downloader.download('maxent_ne_chunker')
nltk.downloader.download('words')
nltk.downloader.download('treebank')
nltk.downloader.download('maxent_treebank_pos_tagger')
nltk.downloader.download('punkt')
nltk.download('averaged_perceptron_tagger')
from spacytextblob.spacytextblob import SpacyTextBlob
import locationtagger
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob');

import matplotlib.pyplot as plt



new_list = []
countries = []
file_name = []

for root, dirs, files in os.walk(r"C:\Deva\Chicago\Quarters\Fall 2022\DAP II\Project\Text processing\UN_cop27"):
    for file in files:
        if file.endswith('.txt'):
            with open(os.path.join(root, file), encoding="utf8") as myfile:
                text = myfile.read()
                document = nlp(text)
                pol = document._.blob.polarity
                new_list.append(pol)
                countries.append(text)
                file_name.append(file)
                
                

sentiment_data = {"SOUTH_SUDAN":new_list[10], "ERITREA":new_list[1], "ETHIOPIA":new_list[2], "INDIA":new_list[3], "KENYA":new_list[4],
                 "NIGERIA":new_list[7], "MALAYSIA":new_list[5], "NAMIBIA":new_list[6], "PERU":new_list[9], "NORWAY":new_list[8], "DENMARK":new_list[0],
                 "SWITZERLAND":new_list[11]}
print(sentiment_data)

keys = sentiment_data.keys()
values = sentiment_data.values()


doc_1 = ''.join(countries)
place_entity = locationtagger.find_locations(text = doc_1)
print("The countries in texts : ")
print(place_entity.countries)



fig, ax = plt.subplots(figsize=(15, 8))
ax.plot(keys, values, linestyle='', marker='o');


ax.set_ylabel('Sentiments')
plt.savefig('Country_sentiments.png',  bbox_inches = 'tight', facecolor='white')