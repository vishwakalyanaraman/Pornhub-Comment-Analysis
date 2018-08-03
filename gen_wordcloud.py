from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt

d = path.dirname(__file__)

text = open(path.join(d, 'CleanedComments.txt')).read()

# Generate a word cloud image
wordcloud = WordCloud().generate(text)

#Second image with a lower font size
wordcloud = WordCloud(max_font_size=40,max_words=2000,normalize_plurals=True).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
