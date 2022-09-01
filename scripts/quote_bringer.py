#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: AR621
This script finds quotes based on search criteria
"""
import os
import sys
import argparse
from itertools import compress
from pprint import pprint  # for that nice list printing :)

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


# %% Function for displaying specific quotes from the repo by provide search criteria
def search_string_list_by_criteria(search_criteria, unfiltered_list):
    filtered_index_list = [False for i in range(len(unfiltered_list))]
    for index in range(len(unfiltered_list)):
        # add condition for the search here
        if search_criteria.lower() in unfiltered_list[index].lower():  # <- .lower() for case "insensiveness"
            filtered_index_list[index] = True
    return filtered_index_list


def preetyprint_filtered_quotes(authors_list, quotes_list):
    if not authors_list:
        pprint("QuoteBringer.py: Found no quotes matching the search criteria")
    else:
        pprint("QuoteBringer.py: Found the following quotes matching the criteria")
        for author, quote in zip(authors_list, quotes_list):
            pprint(author)
            pprint(quote)

# print("quote id: %s" % str(index))
# print(quotes[index])
# print(authors[index])
# print()  # and a lazy newline at the end


# search_quote_by_author('Helen Keller')

parser = argparse.ArgumentParser(description="quote_bringer.py help",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-a", "--author", default='', help="filter output by specific author")
parser.add_argument("-q", "--quote", default='', help="filter output by specific substring in the quotes")
args = vars(parser.parse_args())

# if args[author] != None:

search_filter = search_string_list_by_criteria(args['author'], authors)
search_filter = search_string_list_by_criteria(args['quote'], list(compress(quotes, search_filter)))

filtered_authors = (list(compress(authors, search_filter)))
filtered_quotes = (list(compress(quotes, search_filter)))

preetyprint_filtered_quotes(filtered_authors, filtered_quotes)