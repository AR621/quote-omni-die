# -*- coding: utf-8 -*-
"""
Created on Thu May 12 08:23:04 2022

@author: Killshot
"""

import requests
import json
import collections
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
# %%%% Play with data

quotes = [quote_json.get('quote') for quote_json in quote_jsons]
authors = [quote_json.get('author') for quote_json in quote_jsons]

# %% unique appearances
c = collections.Counter(authors) # we count number of appearances of each author

# %% pie plot
labels = c.keys()
values = c.values()
explode = [0.1]*len(labels)

f=plt.Figure()
ax=plt.pie(
    values,
    rotatelabels=True,
    autopct='%0.1f%%',
    explode=explode,
    labels=labels)
