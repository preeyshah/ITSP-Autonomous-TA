#!/usr/bin/python

import bs4 #to parse from the html code
#import webbrowser
import requests #to get the html code

def find_online(word):
	base = "http://www.dictionary.com/browse/"
	link = base+word
	html_response = requests.get (link)
	html_code = ""
	for chunk in html_response.iter_content (100000):
		html_code+=chunk
	soup = bs4.BeautifulSoup(html_code , "lxml") #make a bs4 object of the code
	type = "Does not exsist"
	a = soup.select('.dbox-pg')
	if len(a) > 0:
		type = a[0].getText() #go through the source code and find out where the lyrics are stored.
	return type

if __name__=="__main__":
	print(find_online("great"))