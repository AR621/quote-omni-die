"""Script used for loading quotes and authors from"""
import requests
import json
import os
from tqdm import tqdm


def load_quotes(download=False, get_authors=False, get_quotes=True, get_size=False):
    # %% Download json's
    if download:
        repo = 'https://raw.githubusercontent.com/AR621/quote-omni-die/main/content/'
        size_file = 'size.json'

        r = requests.get(repo + size_file)
        print(r)

        size_json = json.loads(r.text)
        print(size_json)

        print('fetching json names...')
        quote_json_names = [str(quote_json + 1) + '.json' for quote_json in
                            tqdm(range(size_json.get('number_of_quotes')))]

        print('downloading quotes...')
        quote_requests = [requests.get(repo + quote_json_name) for quote_json_name in tqdm(quote_json_names)]
        print('converting to json\'s')
        quote_jsons = [json.loads(quote_request.text) for quote_request in tqdm(quote_requests)]
    # %% Or use the ones i=you already downloaded 
    else:
        quote_jsons = []

        PATH = os.path.dirname(__file__)[:-7]  # since we don't want to save the jsons in /scripts
        f = open(PATH + '/content/' + 'size' + ".json", 'r')
        size = json.load(f)
        size = size.get('number_of_quotes')

        for i in tqdm(range(size)):
            f = open(PATH + '/content/' + str(i + 1) + ".json", 'r')
            new_json = json.load(f)
            quote_jsons.append(new_json)

    if get_quotes:
        quotes = [quote_json.get('quote') for quote_json in quote_jsons]
        return quotes
    if get_authors:
        authors = [quote_json.get('author') for quote_json in quote_jsons]
        return authors
    # TODO  make em handle both quaries at once

def get_size(download=False):
    if download:
        repo = 'https://raw.githubusercontent.com/AR621/quote-omni-die/main/content/'
        size_file = 'size.json'
        r = requests.get(repo + size_file)
        print(r)
        return json.loads(r.text).get('number_of_quotes')
    else:
        PATH = os.path.dirname(__file__)[:-7]  # since we don't want to save the jsons in /scripts
        f = open(PATH + '/content/' + 'size' + ".json", 'r')
        return json.load(f).get('number_of_quotes')
