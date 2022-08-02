# -*- coding: utf-8 -*-
"""
@author: Killshot
"""

import collections
import os
import matplotlib.pyplot as plt
from sys import path

# user
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
c = collections.Counter(authors)  # we count number of appearances of each author
c = sorted(c.items(), key=lambda x: x[1])  # sort the dictionary so when displayed on...
# ...pie chart it looks well-ordered
c = dict(c)
# %% Validity check
c = collections.Counter(authors)  # we count number of appearances of each author
c = sorted(c.items(), key=lambda x: x[1])  # sort the dictionary so when displayed on pie chart
# it looks well-ordered
c = dict(c)
# %% pie plot

labels = c.keys()
values = c.values()
explode = [0.6 / appearances for appearances in values]  # the bigger the slice the closer it will be to the center

f = plt.Figure(figsize=(48, 48))

patches, labels, pct_texts = plt.pie(
    values,
    rotatelabels=True,
    radius=0.75,
    autopct='%0.1f%%',
    explode=explode,
    startangle=-180,
    labels=labels,
    textprops={'fontsize': 7})
# rotate the percentage label same way as author label
for label, pct_text in zip(labels, pct_texts):
    pct_text.set_rotation(label.get_rotation())
plt.tight_layout()
if SAVE:
    plt.savefig('figures/pie-stats.png', dpi=400)
if DISP:
    plt.show()
