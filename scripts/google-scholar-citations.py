# [Mar 2019, LAB] adapted from psi4meta/recent-citing-articles/parse_gs_psi4_refs.py by CDS

# this program creates a list of recent papers citing the Psi4 1.1 paper
# and creates a webpage with this info, suitable for posting at
# psicode.org

# January 2018, C. David Sherrill


import os
import re
import sys
import json
from urllib.parse import quote

import bs4
import yaml
import requests


with open(f'../data/pubs/psi_software.yaml') as fp:
    ydict = yaml.safe_load(fp)

results = {}

for psipub in ydict:
    results[psipub['short']] = {}
    print("pub", psipub["short"])

    # pull over the Google Scholar webpage for the article, scisbd=1 means 'sort by date' (most recent articles first)
    page1_of_citing_articles = f"""https://scholar.google.com/scholar?cites={psipub['gs']}&hl=en&scipsc=&q=&scisbd=1"""
    article_summary = """https://scholar.google.com/scholar?hl=en&as_sdt=0%2C11&q={}&btnG=""".format(quote(psipub['title']))

    ## total citation count
    res = requests.get(article_summary)
    res.raise_for_status()

    citedby = re.search('Cited by (\d+)', res.text)
    print("citedby", citedby.groups())
    print("page1", page1_of_citing_articles)
    print("summ", article_summary)
    print("results", results)
    results[psipub['short']]['citation_count'] = int(citedby[1])

    ## recent few citing articles
    res = requests.get(page1_of_citing_articles)
    res.raise_for_status()

    # parse the webpage into elements
    # * get list of titles with links
    # * we seem to be getting an extra title lately (our own) for no apparent reason... pop that off
    # * get the list of authors (and journal)
    parsed = bs4.BeautifulSoup(res.text, "html.parser")
    titles = parsed.select('.gs_rt a')
    titles.pop(0)
    authors = parsed.select('.gs_a')

    results[psipub['short']]['most_recent'] = {
        'link': titles[0].get('href'),
        'title': titles[0].getText(),
        'authors': authors[0].getText(),
    }

with open(f'../data/pubs/google_scholar_citations.json', 'w') as fp:
    json.dump(results, fp, indent=4, sort_keys=True)
