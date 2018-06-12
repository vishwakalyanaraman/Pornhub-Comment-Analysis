import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

def commentData():
	comment = {}
	comments_list = []
	links_list = []
	#Starting URL (can be changed later)
	url = "https://www.pornhub.com/view_video.php?viewkey=2006034279"
	BASE_URL = "https://www.pornhub.com"
	resp = requests.get(url)
	if resp.status_code == 200:
		print("**********Successfully connected**********")
		soup = BeautifulSoup(resp.text, 'html.parser')
    	
    	#Getting comments
		for comment_block in soup.findAll("div", {"class" : "commentMessage"}):
			i = 0
			comment = comment_block.findAll("span")[i]
			comments_list[i] = comments_list.extend(comment)
			i+=1
	#Getting video links
		for a_tag in soup.find_all("a", href=True):
			i = 0
			url2 = a_tag.attrs["href"]
			if isVideo(url2):
				links_list[i] = links_list.append(BASE_URL+url2)
			i+= 1
	else:
		print("Error connecting")

	df = pd.DataFrame(comments_list)
	df.columns =['Comments']

	df2 = pd.DataFrame(links_list)
	df2.columns = ['Links']

	return (df, df2)

def isVideo(url):
	#Validates text in the form: 
	#www.pornhub.com/view_video.php?viewkey=SOMETEXT
    return True if "/view_video.php?viewkey=" in url else False

def cleanLinks(df):
	res = df[df.Links.str.startswith('https://www.pornhub.com/view',na = False)]
	return res
def cleanComments(df):

    #Removing hyperlinks and double quotes
    df['Comments'] = df['Comments'].str.replace('"','')
    df['Comments'] = df['Comments'].str.replace(r"\<.*\>","")
    df['Comments'] = df['Comments'].str.replace(r"\[.*\]","")
    df['Comments'] = df['Comments'].replace('',np.nan)
    df.dropna(inplace = True)

    #Changing case to lower for all strings
    df['Comments'] = df['Comments'].str.lower()

    #df.csv('cleaned2.csv')
    return df

Old_Comments, Old_Links  = commentData()
New_Comments = cleanComments(Old_Comments)
New_Links = cleanLinks(Old_Links)

New_Links.reset_index(drop=True, inplace=True)
New_Comments.reset_index(drop=True, inplace=True)

print('******SAMPLE DATA******')
print(New_Comments.head())
print(New_Links.head())
