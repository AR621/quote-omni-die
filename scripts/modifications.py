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
import sys
import matplotlib.pyplot as plt
from tqdm import tqdm

# own imports
# paths (so the script works when invoked out of its own dir)
file_path = os.path.abspath(__file__)
file_name = os.path.basename(__file__)
file_path=file_path[:-len(file_name)]
sys.path.insert(0, file_path)
# finalle here...
import load_quotes as loader

# quote_jsons=load_quotes()
    
# %% create quote and uthor lists from loaded json's
quote_jsons = loader.load_quotes()
authors = [quote_json.get('author') for quote_json in quote_jsons]
quotes = [quote_json.get('quote') for quote_json in quote_jsons]

# %% Measuring simularity between quotes for administrative purposes
import numpy
import difflib

def string_simularity(string_list):
    difference_matrix = numpy.eye(len(string_list))
    pivot=0
    for qi1 in range(len(quotes)):
        for qi2 in range(pivot,len(quotes)):
           difference_matrix[qi1,qi2] = difflib.SequenceMatcher(None, quotes[qi1], quotes[qi2]).ratio()
        pivot+=1
        # in general we use the pivot to help us reduce calculation time, we dont need
        # to create a whole diff. matrix, we only need one (triangular) half of it :)
    return difference_matrix

difference = string_simularity(quotes)
# %% Filtering simularity so we can easly see which quotes are simular to each other
def filter_by_simularity(difference_matrix, tolerance=0.4):
    simular_quotes=numpy.empty([0,3],dtype=float)
    with numpy.nditer(difference_matrix, flags=["multi_index"]) as it:
        for simularity_measure in it:
            if( (simularity_measure >= tolerance) and (len(set(it.multi_index)) != 1)):
                simular_quotes=numpy.append(simular_quotes, [[it.multi_index[0]+1, it.multi_index[1]+1, simularity_measure]], axis=0)
    return simular_quotes

simular_quotes_list=filter_by_simularity(difference, tolerance=0.5) # not really a list but the name still suits it...
simular_quotes_list_sorted=simular_quotes_list[simular_quotes_list[:,2].argsort()]
print(simular_quotes_list_sorted[::-1])
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
