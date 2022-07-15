#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 20:58:24 2022

@author: Killshot
"""
import json
import os
import sys

# own imports
# paths (so the script works when invoked out of its own dir)
file_path = os.path.abspath(__file__)
file_name = os.path.basename(__file__)
file_path = file_path[:-len(file_name)]
sys.path.insert(0, file_path)
# finally here...
import load_quotes as loader
import string_comparison as sc

# quote_jsons=load_quotes()

# %% create quote and author lists from loaded json's
authors = loader.load_quotes(get_quotes=False, get_authors=True)
quotes = loader.load_quotes(get_quotes=True, get_authors=False)

# %% MEC - Mass Error Correction

# Opening JSON file
swap_criteria = 'Epicteus'

for index in range(len(authors)):

    # add condition for the search here    
    if authors[index] == swap_criteria:
        authors[index] = 'Epictetus'
        print('changed item with id %i' % (index + 1))
        # and finally save the modified json
        new_json_dict = {"author": authors[index], "quote": quotes[index]}
        # output 
        # PATH = "../content/"
        PATH = os.path.dirname(__file__)[:-7]  # since we don't want to save the jsons in /scripts
        with open(PATH + '/content/' + str(index + 1) + ".json", 'w') as f:
            json.dump(new_json_dict, f)
        # Closing file
        f.close()
