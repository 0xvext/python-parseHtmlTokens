#!/bin/python3

# Required libraries for objects used
import requests
from bs4 import BeautifulSoup

# Static cookie value
cookie = {'progress': 'PROGRESSCOOKIEHERE'}

# Create a requests object containing the results of a GET request
r = requests.get('https://SITEHERE', cookies=cookie)

# Create a soup object to parse the results
soup = BeautifulSoup(r.text, 'html.parser')

# Loop through 100 batch requests (limited to 100 tokens at a time by page)
for i in range (100):
	# Loop through object contents elements 3 through 103 (unique to HTML used by page)
	for i in range (3, 103):
		with open("test.txt", "a") as myfile:
		    myfile.write(soup.contents[i] + "\n")
