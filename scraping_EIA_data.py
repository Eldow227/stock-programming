# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 19:27:02 2021

@author: kmate
"""

import pandas as pd
import numpy as np
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

url = "https://www.eia.gov/dnav/ng/hist/n9010us2m.htm"
html = urlopen(url)

soup = BeautifulSoup(html, 'lxml')

rows = soup.find_all('tr')
for row in rows:
    row_td = row.find_all('td')
# %%
import re

list_rows = []
for row in rows:
    cells = row.find_all('td')
    str_cells = str(cells)
    clean = re.compile('<.*?>')
    clean2 = (re.sub(clean, '',str_cells))
    list_rows.append(clean2)
for i in list_rows:
    if i.startswith('[\xa0\xa0'):
        i.replace('[\xa0\xa0', "values")
        
print(list_rows)
# %%
for row in rows:
    row_td = row.find_all('td')
    cleantext = BeautifulSoup(str(row_td), "lxml").get_text()
    print(cleantext)
    
        

