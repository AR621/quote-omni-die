#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 20:58:24 2022

@author: Killshot
"""
import requests
import json
import collections
import os
import matplotlib.pyplot as plt

from tqdm import tqdm

# %% Download json's
repo='https://raw.githubusercontent.com/AR621/quote-omni-die/main/content/'
size_file='size.json'

r = requests.get(repo + size_file)
print(r)

size_json = json.loads(r.text)
print(size_json)

print('fetching json names...')
quote_json_names = [str(quote_json+1) + '.json' for quote_json in tqdm(range(size_json.get('number_of_quotes')))]

print('downloading quotes...')
quote_requests = [requests.get(repo+quote_json_name) for quote_json_name in tqdm(quote_json_names)]
print('converting to json\'s')
quote_jsons = [json.loads(quote_request.text) for quote_request in tqdm(quote_requests)]
# %% Or use the ones i=you already downloaded 
quote_jsons=[]

PATH = os.path.dirname(__file__)[:-7] # since we don't want to save the jsons in /scripts
f=open(PATH + '/content/' + 'size' + ".json", 'r')
size=json.load(f)
size=size.get('number_of_quotes')
    
for i in tqdm(range(size)):
    f=open(PATH + '/content/' + str(i+1) + ".json", 'r')
    new_json=json.load(f)
    quote_jsons.append(new_json)
    
# %% create quote and uthor lists from loaded json's
authors = [quote_json.get('author') for quote_json in quote_jsons]
quotes = [quote_json.get('quote') for quote_json in quote_jsons]

# %% Measuring simularity between quotes for administrative purposes
import numpy
import difflib

def string_simularity(string_list):
    difference_matrix = numpy.eye(len(string_list))
    for qi1 in range(len(quotes)):
        for qi2 in range(len(quotes)):
           difference_matrix[qi1,qi2] = difflib.SequenceMatcher(None, quotes[qi1], quotes[qi2]).ratio()
    return difference_matrix
difference = string_simularity(quotes)

# %% MEC - Mass Error Correction
import json 
# Opening JSON file
swap_criteria = 'Epicteus'

for index in range(len(authors)):
    
    # add condition for the search here    
    if authors[index] == swap_criteria:
        authors[index] = 'Epictetus'
        print('changed item with id %i' %(index+1))
        # and finally save the modified json
        new_json_dict ={"author":authors[index],"quote":quotes[index]}
        # output 
        # PATH = "../content/"
        PATH = os.path.dirname(__file__)[:-7] # since we don't want to save the jsons in /scripts
        with open(PATH + '/content/' + str(index+1) + ".json", 'w') as f:
            json.dump(new_json_dict, f)
            
# Closing file
f.close()