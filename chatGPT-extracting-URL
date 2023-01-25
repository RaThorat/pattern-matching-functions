#Original code Extracting hyperlinks from pdfs
#https://www.tutorialspoint.com/extract-hyperlinks-from-pdf-in-python
def find_url(string):
  #Find all the String that matches with the pattern
  regex = r"(https?://\S+)"
  url = re.findall(regex,string)
  for url in url:
     return url
     

#chatGPT update version of the code from original file

import re

def find_url(string):
    urls = re.findall(r"(https?://\S+)", string)
    return urls

#This updated version of the code makes the following changes:

#Renamed the variable url to urls to better reflect that it is a list of URLs.
#Use findall method to find all the URLs that match the pattern and return them in a list.
#Use return statement to return the list of URLs.

# You can also use re.compile to define the regular expression pattern once and reuse it multiple times.

import re

url_pattern = re.compile(r"(https?://\S+)")

def find_url(string):
    urls = url_pattern.findall(string)
    return urls

# Also you can use urllib package to extract URLs from pdfs.

from urllib.parse import urlparse

def find_url(string):
    urls = [url for url in string.split() if urlparse(url).scheme]
    return urls

#This will give you a list of URLs in the text, but be aware that the URLs found in the text may not be valid.
