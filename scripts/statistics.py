# -*- coding: utf-8 -*-
"""
@author: Killshot
"""

import collections
import os
import matplotlib.pyplot as plt
import pprint

from numpy import arange
from sys import path

# user
# TODO make em go from cli args
DISP = False
SAVE = True

# own imports
# paths (so the script works when invoked out of its own dir)
file_path = os.path.abspath(__file__)
file_name = os.path.basename(__file__)
file_path = file_path[:-len(file_name)]
path.insert(0, file_path)
# finally here...
import load_quotes as loader

# %%%% Play with data
authors = loader.load_quotes(get_quotes=False, get_authors=True)
quotes = loader.load_quotes(get_quotes=True, get_authors=False)

# %% unique appearances
author_appearances = collections.Counter(authors)  # we count number of appearances of each author
author_appearances = sorted(author_appearances.items(), key=lambda x: x[1])  # sort the dictionary so when displayed on...
# ...pie chart it looks well-ordered
author_appearances = dict(author_appearances)
# %% pie plot

labels = author_appearances.keys()
values = author_appearances.values()

# filter authors which appear in less than 1% of quotes
most_common_authors=dict(author_appearances)
most_common_authors['other']=0
least_common_authors=dict(author_appearances)

for (author, num_of_quotes) in author_appearances.items():
    treshold=0.01*loader.get_size()
    if(num_of_quotes<=treshold):# filter out authors with less than 1% input and append their input to 'other' key
        most_common_authors.pop(author)
        most_common_authors['other'] = most_common_authors['other']+num_of_quotes
    else:
        least_common_authors.pop(author)


explode = [0.6 / appearances for appearances in most_common_authors.values()]  # the bigger the slice the closer it will be to the center
f = plt.Figure(figsize=(48, 48))

patches, labels, pct_texts = plt.pie(
    most_common_authors.values(),
    rotatelabels=True,
    radius=0.75,
    autopct='%0.1f%%',
    explode=explode,
    startangle=-90,
    labels=most_common_authors.keys(),
    textprops={'fontsize': 7})
# rotate the percentage label same way as author label
for label, pct_text in zip(labels, pct_texts):
    pct_text.set_rotation(label.get_rotation())
plt.tight_layout()
if SAVE:
    plt.savefig('figures/pie-stats.png', dpi=400)
if DISP:
    plt.show()