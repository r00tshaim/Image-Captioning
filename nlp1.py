'''
NLP

analyzing text(basically working with text)

text can be books,reviews,html text got from web scarping

its a brach of ML

tools used:numpy,matplotlib.pyplot,pandas

steming->grouping word eg:treating loved as love 
'''

import numpy as numpy
import matplotlib.pyplot as plt
import pandas as pd

#importing dataset
dataset = pd.read_csv('Restaurant_Reviews.tsv', delimiter='\t', quoting=3)
#print(dataset)

#cleaning text
import re #to clean text

#corpus is list of coomon words in NLP which contains text
corpus=[]
for i in range(0,1000):
	#cleaning first review
	#sub funtion- substitues any char other than a-zA-Z with space
	review = re.sub('[^a-zA-Z]',' ',dataset['Review'][i])

	#to convert it to lower case
	review = review.lower() 

	#libary to removing unwanted words from reivew
	import nltk
	#stopwords is list of irrevleant words present in review
	nltk.download('stopwords')
	from nltk.corpus import stopwords
	#split the review in diff words so that it becomes list of words
	review = review.split()

	#removing unwnated words from review
	review = [word for word in review if not word in set(stopwords.words('english'))]

	#steming->taking the root word
	#eg loved->love is same for positive review

	#applying stem function to each words of our review


	#importing librabry to perform steaming
	from nltk.stem.porter import PorterStemmer

	#object of PorterStemmer
	ps=PorterStemmer()

	#appplying stemming on each word
	review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]

	#before-->['wow', 'loved', 'place']
	#after-->['wow', 'love', 'place']

	#joining the words in list and making it a string
	review = ' '.join(review)

	#appeding to corpurus
	corpus.append(review)



#Creating Bag of Words model-->is review positive or negative

#tokeniztion-->take each from sentence(here review sentence) and create column for each word

	