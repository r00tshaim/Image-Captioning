# Intro To NLP

**NLP is all about playing with text or we can say analyzing text(basically working with text)**

*text can be books,reviews,html text got from web scarping*

*it is a brach of ML*

*tools used:pandas(to read csv files),nltk(text prcressing library)*

*steming->grouping word eg:treating loved as love*


## Simple Steps to follow in NLP:

suppose we are dealing with 'resturants reviews'

1.read reviews(using pandas)

2.cleaning text means removing unwated things like colons,commas,etc and take only text ie from a-zA-Z(using re)

>eg:Wow..... this is amazing!
>output:Wow this is amazing

3.conveting all text to lower case(using .lower() function)

>eg:Wow this is amazing
>output:wow this is amazing

4.removing unwanted words(using corpus(corpus are nothing but list of unwanted words eg.this,is,having,etc...) from nltk library)

>eg:this place is amazing
>output:place amazing

5.taking only root words from sentence(using PorterStemmer from nltk)
this is known as stemming process in NLP

>eg:['wow', 'loved', 'place']
>output:['wow', 'love', 'place']



