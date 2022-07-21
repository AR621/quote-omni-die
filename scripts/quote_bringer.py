#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: AR621
This script finds quotes based on search criteria
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

# %% create quote and author lists from loaded json's
authors = loader.load_quotes(get_quotes=False, get_authors=True)
quotes = loader.load_quotes(get_quotes=True, get_authors=False)


# %% Function for displaying specific author quotes from the repo
def search_quote_by_author(search_criteria):
    for index in range(len(authors)):
        # add condition for the search here
        if authors[index] == search_criteria:
            print("quote id: %s" % str(index))
            print(quotes[index])
            print(authors[index])
            print()


search_quote_by_author('Aristotle')