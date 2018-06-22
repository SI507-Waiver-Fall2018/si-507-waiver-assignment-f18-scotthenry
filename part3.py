
# coding: utf-8

# In[1]:

#Stanley Scott Henry (schenry) 81390908

# these should be the only imports you need

import requests
from bs4 import BeautifulSoup

# write your code here
# usage should be python3 part3.py

#Set up beautiful soup
site_url = 'http://michigandaily.com'
r = requests.get(site_url)
soup = BeautifulSoup(r.text, "lxml")

#Retrieve a list of the articles
articles_URLS = soup.find(class_ = "view-most-read").findAll("a")

#Iterates thorugh each URL printing title & author
for URL in articles_URLS:
    r = requests.get(site_url + URL['href'])
    soup = BeautifulSoup(r.text, "lxml")
    
    #Grabs the title
    title = soup.find("title")
    print(title.text.split("|")[0])
    
    #Try/except to handle articles without authors
    try:
        author = soup.find(class_ = "byline").find(class_ = "link")
        print("by: ", author.text)
    except:
        print("by: Unlisted")

