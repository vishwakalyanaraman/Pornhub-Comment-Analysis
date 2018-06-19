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

	df = pd.DataFrame(comments_list)
	df.columns =['Comments']

	return (df)

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

Old_Comments  = commentData()
New_Comments = cleanComments(Old_Comments)
New_Comments.reset_index(drop=True, inplace=True)

print('******SAMPLE DATA******')
print(New_Comments.head())

New_Comments.csv('CleanedComments.csv')
