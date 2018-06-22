import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

def fetchingLinks():
	links =[]
	url = "https://www.pornhub.com/view_video.php?viewkey=2006034279"
	BASE_URL = "https://www.pornhub.com"
	resp = requests.get(url)
	if resp.status_code == 200:
		print("Successfully connected")
		soup = BeautifulSoup(resp.text, 'html.parser')

	#Getting Links
		for tag in soup.find_all('a', href=True):
			i = 0
			url2 = tag.attrs['href']
			links[i] = links.append(BASE_URL+url2)
			i += 1

	else:
		print("Error connecting")

	df = pd.DataFrame(links)
	df.columns = ['Links']

	#Cleaning data
	df = df[df.Links.str.startswith('https://www.pornhub.com/view', na = False)]
	df.drop_duplicates(inplace=True)
	df.reset_index(drop=True, inplace=True)
	return df

LinksDF = fetchingLinks()

#Export to CSV
LinksDF.to_csv("CleanedLinks.csv")

