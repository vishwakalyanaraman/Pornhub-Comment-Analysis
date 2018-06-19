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

The data is cleaned using Pandas with the following code:

```
df['Comments'] = df['Comments'].str.replace('"','')
df['Comments'] = df['Comments'].str.replace(r"\<.*\>","")
df['Comments'] = df['Comments'].str.replace(r"\[.*\]","")
df['Comments'] = df['Comments'].replace('',np.nan)
df.dropna(inplace = True)
df['Comments'] = df['Comments'].str.lower()
```
