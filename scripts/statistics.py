# -*- coding: utf-8 -*-
"""
Created on Thu May 12 08:23:04 2022

@author: Killshot
"""

import requests
import json
import collections
import os
import sys
import matplotlib.pyplot as plt
from tqdm import tqdm

# own imports
# paths (so the script works when invoked out of its own dir)
file_path = os.path.abspath(__file__)
file_name = os.path.basename(__file__)
file_path=file_path[:-len(file_name)]
sys.path.insert(0, file_path)
# finally here...
import load_quotes as loader
# %%%% Play with data
quote_jsons = loader.load_quotes()

quotes = [quote_json.get('quote') for quote_json in quote_jsons]
authors = [quote_json.get('author') for quote_json in quote_jsons]

# %% unique appearances
c = collections.Counter(authors) # we count number of appearances of each author
c = sorted(c.items(), key=lambda x:x[1]) # sort the dictionary so when displayed on...
# ...pie chart it looks well-ordered
c = dict(c)
# %% Validity check
c = collections.Counter(authors) # we count number of appearances of each author
c = sorted(c.items(), key=lambda x:x[1]) # sort the dictionary so when displayed on pie chart
# it looks well-ordered
c = dict(c)
# %% pie plot

labels = c.keys()
values = c.values()
explode = [0.6/appearances for appearances in values] # the bigger the slice the closer it will be to the center

f = plt.Figure(figsize=(48,48))
f.show()
patches, labels, pct_texts = plt.pie(
    values,
    rotatelabels=True,
    autopct='%0.1f%%',
    explode=explode,
    startangle=-180,
    labels=labels)
# rotate the percentage label same way as author label
for label, pct_text in zip(labels, pct_texts):
    pct_text.set_rotation(label.get_rotation())