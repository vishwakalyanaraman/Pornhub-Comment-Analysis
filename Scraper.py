import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup
import csv

def commentData():
	comment = {}
	i = 0
	comments_list1 = []
	comments_list = []
	xyz = []
	links_list = []
	#df = pd.DataFrame({'Comments':[]})
	urls = pd.read_csv("CleanedLinks.csv",index_col=0)
	url_list = list(urls.values.flatten())
	for x in url_list:
		#url1 = column.loc[1]
		url = "https://www.pornhub.com/view_video.php?viewkey=2006034279"
		BASE_URL = "https://www.pornhub.com"
		resp = requests.get(x)
		if resp.status_code == 200:
			#print("**********Successfully connected**********")
			soup = BeautifulSoup(resp.text, 'html.parser')
	    	
	    	#Getting comments
			for comment_block in soup.findAll("div", {"class" : "commentMessage"}):
				i = 0
				comment = comment_block.findAll("span")[i]
				#df.append(comment)
				comments_list[i] = comments_list.extend(comment)
				i+=1
			xyz = comments_list
			comments_list1.extend(xyz)

		print("Total number of comments (before cleaning) are "+str(len(comments_list1)))
		
		df = pd.DataFrame(comments_list, columns=['Comments'])
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

print("Total number of comments (after cleaning) are " + str(New_Comments.size))

print('\n+******SAMPLE DATA******')
print(New_Comments.head())

print("Exporting file to CSV...",flush = True)
New_Comments['Comments'].to_csv('CleanedComments.csv')


#Convert CSV to TXT for easy wordcloud

print("Exporting file to TXT...",flush = True)
csv_file = "CleanedComments.csv"
txt_file = "CleanedComments.txt"
with open(txt_file, "w") as my_output_file:
	with open(csv_file, "r") as my_input_file:
		 [ my_output_file.write(" ".join(row)+'\n') for row in csv.reader(my_input_file)]
	my_output_file.close()

