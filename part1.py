
# coding: utf-8

# In[1]:

#Stanley Scott Henry (schenry) 81390908

# these should be the only imports you need
import tweepy
import nltk
import json
import sys
import re

consumer_key = 'rIvYnZRB4dV3vh2ZeGxIJ69Ve'
consumer_secret = 'RIl25lDaHj1VPaO5LkCSPdcutUEQ7QKbJExh1Cb4UOjHTE8JoY'
access_token = '1627053481-Xn9xloRFLF9g7byv0SvV7znZ5v6d5LZaH5rZbQc'
access_token_secret = 'qh4iEO6dUGEiCiTfdPFE1EPO4pkrxprHuxC7XsPxEAowH'

# write your code here
# usage should be python3 part1.py <username> <num_tweets>

user_name = sys.argv[1]
num_tweets = int(sys.argv[2])

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#Get a list of all tweets
all_tweets = []
for tweet in tweepy.Cursor(api.user_timeline,id=user_name, tweet_mode='extended').items(num_tweets):
     all_tweets.append(tweet)

#Pull out the original tweets and count favourites/retweets 
favourite_count = 0
retweet_count = 0
original_count = 0

for tweet in all_tweets:
    if not hasattr(tweet, 'retweeted_status'):
        original_count += 1
        favourite_count += tweet.favorite_count
        retweet_count += tweet.retweet_count

#Get all of the text, join it and clean it
all_tweets_text = []

#get the full text of both tweets, from two different places
for tweet in all_tweets:
    if hasattr(tweet, 'retweeted_status'):
        all_tweets_text.append(tweet.retweeted_status.full_text)
    else: 
        all_tweets_text.append(tweet.full_text)
        
#merge it into one long string
all_tweets_string = ' '.join(all_tweets_text)

#Tokenize
list_tokens = nltk.tokenize.word_tokenize(all_tweets_string)

#Tag them
list_tags = nltk.pos_tag(list_tokens)

#filter out stop words and ensure alphanumeric characters
list_nouns = []
list_verbs = []
list_adjectives = []

clean_tags = []
stop_words = ['RT', 'rt', 'http', 'https', 's', 'S']

for pos in list_tags:
    if pos[0] not in stop_words and pos[0][0].isalpha():
        clean_tags.append(pos)

#sort into nouns/verbs/adjectives
for pos in clean_tags:
    if (pos[1][:2] == 'VB'):
        list_verbs.append(pos[0])
    elif (pos[1][:2] == 'JJ'):
        list_adjectives.append(pos[0])
    elif (pos[1][:2] == 'NN'):
        list_nouns.append(pos[0])

#count the types
frequent_nous = nltk.FreqDist(list_nouns).most_common(5)           
frequent_verbs = nltk.FreqDist(list_verbs).most_common(5)
frequent_adjectives = nltk.FreqDist(list_adjectives).most_common(5)

#printer function
def frequent_printer(words):
    for word in words:
        print(word[0]+ "("+ str(word[1]) +") ", end="")
    print('\r')

print("USER: ", user_name)
print("TWEETS ANALYZED: ", len(all_tweets))

print("ADJECTIVES: ", end="")
frequent_printer(frequent_adjectives)
print("VERBS: ", end="")
frequent_printer(frequent_verbs)
print("NOUNS: ", end="")
frequent_printer(frequent_nous)

print("ORIGINAL TWEETS: ", original_count)
print("TIMES FAVORITED (ORIGINAL TWEETS ONLY): ", favourite_count)
print("TIMES RETWEETED (ORIGINAL TWEETS ONLY): ", retweet_count)

#export noun csv
import csv
noun_export = frequent_nous
noun_export.insert(0, ("Noun", "Number"))
myFile = open('noun_data.csv', 'w')
with myFile:
    writer = csv.writer(myFile)
    writer.writerows(noun_export)

