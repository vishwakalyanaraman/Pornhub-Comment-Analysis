# PornHub Comment Analysis
This project scrapes data from PornHub videos and analyses them using Machine Learning and other Data Science tools

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

The following packages are required in order to implement this project

- `pandas`
- `BeautifulSoup`
- `matplotlib`

# Step 1: Collecting Links

The very first step in analysing comments is to collect links of videos. To do so I have written a
script ```link_collector.py```. This script collects all links from a video's page and cleans the
data into a CSV file.

# Step 2: Collecting Comments

Once the links have been collected we can start extracting the comments from each video. This is
done with the ```scraper.py``` script. The scraper finds all comments in a video and extracts them
into a CSV file.

### Cleaning the data

When collecting comments, most of them were HTML or CSS tags which needed to be removed before
processing.
The data is cleaned using Pandas with the following code:

```
df['Comments'] = df['Comments'].str.replace('"','')
df['Comments'] = df['Comments'].str.replace(r"\<.*\>","")
df['Comments'] = df['Comments'].str.replace(r"\[.*\]","")
df['Comments'] = df['Comments'].replace('',np.nan)
df.dropna(inplace = True)
df['Comments'] = df['Comments'].str.lower()
```

# Step 3: Generating WordCloud

Once the final CSV of comments is made the program ```gen_wordcloud.py``` helps in making two
different wordclouds of different sizes. The size of a word determines how frequently that word
occurs in the comments. 

![alt_text](/Examples/figure1.png)
# Step 4: Further works

I will be working on correlating words with genres and possibly performing sentiment analysis on the
comments to determine the ratio of postive to negative comments. There is tons of scope in terms of
producing interesting graphs with this data.

