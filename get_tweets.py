import tweepy 
import configparser
import datetime


#read credential from config.ini

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']
access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

#authenticate app to twitter API

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

#get first 5 tweets
for i in range(4):
    print(public_tweets[i].text)
print('\n')

#searching hashtag
tweets = tweepy.Cursor(api.search_tweets,q=input('Enter word: '), lang="en",since_id=input('Enter Time in yyyy-mm-dd: '),tweet_mode='extended').items(50)
list_tweets = [tweet for tweet in tweets]
for tweet in list_tweets:
    username = tweet.user.screen_name
    hashtags = tweet.entities['hashtags']
hashtext = list()
for j in range(0, len(hashtags)):
    hashtext.append(hashtags[j]['text'])
ith_tweet = [username, hashtext]
print(ith_tweet)

