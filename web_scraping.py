#libraries
#step1
import numpy as np
import pandas as pd
import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup
#step2

# for getting the header from
# the HTML file
content = urlopen('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')
bsObj = BeautifulSoup(content)

"""
content = getHTMLContent('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')
tables = content.find_all('table')
table = content.find('table', {'class': 'wikitable sortable'})

"""

list_of_rows = []

for row in bsObj.findAll('tr'):
    list_of_cells = []
    for cell in row.findAll(["th","td"]):
        text = cell.text
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells) 

list_of_rows.pop(1)

with open('populationtable.csv', 'w') as file: 
    write = csv.writer(file) 
    write.writerows(list_of_rows) 
   
df = pd.read_csv('populationtable.csv' , header= 0, encoding= 'unicode_escape')

with open("populationtable.csv", 'rb') as f:
  text = f.read().decode(errors='replace')  

print(text)  
# ||  print(df) 
  
