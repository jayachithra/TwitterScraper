# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 13:41:08 2018

@author: Jaya
"""

import tweepy
from tweepy import OAuthHandler
from tweepy import Cursor
from datetime import datetime, date, time, timedelta
import csv
# 

from tweepy import Stream
from tweepy.streaming import StreamListener


consumer_key = '1A00LLlOgMFICokeh5sX4FjAy'
consumer_secret = 'zzHUPTjjrj5Yk2PbeGVMgZeEQYPrQkasg8ZHw0BVcUChTsbIPr'
access_token = '297866831-VspDhxwUHFGvWt0ci3F88jEhoRqXGyYl7AEfaVOM'
access_secret = 'h1xZuwWvDYlNDvSLPb7uxO2GI2wxeBZxxxAPt8ItNJsXV'
# 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
auth_api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
# 
#api = tweepy.API(auth)
#
#def process_or_store(tweet):
#    print(tweet)
#
#for status in tweepy.Cursor(api.home_timeline).items(10):
#    # Process a single status
#    print(status.text)
#    print('------')
#    #process_or_store(status._json)


 
#class MyListener(StreamListener):
# 
#    def on_data(self, data):
#        try:
#            with open('python.json', 'a') as f:
#                f.write(data)
#                return True
#        except BaseException as e:
#            print("Error on_data: %s" % str(e))
#        return True
# 
#    def on_error(self, status):
#        print(status)
#        return True
# Open/Create a file to append data
with open('brand24_tweets.csv','a') as f:

 #Use csv Writer
 csvWriter = csv.writer(f)
 csvWriter.writerow(['Account name', 'Date Tweeted', 'Tweet','Media url'])
    
 account_list = ['brand24']
 if len(account_list) > 0:
  for target in account_list:
    print("Getting data for " + target)
    item = auth_api.get_user(target)
    print("name: " + item.name)
    print("screen_name: " + item.screen_name)
    print("description: " + item.description)
    print("statuses_count: " + str(item.statuses_count))
    print("friends_count: " + str(item.friends_count))
    print("followers_count: " + str(item.followers_count))
    
    tweet_count = 0
    #end_date = datetime.utcnow() - timedelta(days=186)
    end_date = datetime.strptime('Apr 1 2018  1:00AM', '%b %d %Y %I:%M%p')
    for status in Cursor(auth_api.user_timeline, id=target).items():
     tweet_count += 1
     #print(tweet_count)
     media_url = ''
     media = status.entities.get('media', [])
     if(len(media) > 0):
         media_url = media[0]['media_url']
         
     if(target != 'Charles_SEO' and target != 'brightonseo' and target != 'anton_shulke' and target != 'semrush'):
         if (not status.retweeted) and ('RT @' not in status.text):
             #print("Not retweeted")
             #print(status.text)
             csvWriter.writerow([status.user.screen_name, status.created_at,status.text.encode('utf-8'),media_url])
     else:
       csvWriter.writerow([status.user.screen_name, status.created_at,status.text.encode('utf-8'),media_url])
   
    
         
#     if hasattr(status, "entities"):
#        entities = status.entities
#        #print(entities)
#        print("--")
#        if "hashtags" in entities:
#          for ent in entities["hashtags"]:
#            if ent is not None:
#              if "text" in ent:
#                hashtag = ent["text"]
#                #if hashtag is not None:
#                  #hashtags.append(hashtag)
#        if "user_mentions" in entities:
#          for ent in entities["user_mentions"]:
#            if ent is not None:
#              if "screen_name" in ent:
#                name = ent["screen_name"]
#                #if name is not None:
#                  #mentions.append(name)
     if status.created_at < end_date:
        break

f.close()
     
#twitter_stream = Stream(auth, MyListener())
#twitter_stream.filter(track=['#python'])
#for tweet in tweepy.Cursor(api.search,q="#unitedAIRLINES",count=100,
#                           lang="en",
#                           since="2017-04-03").items():
#    print (tweet.created_at, tweet.text)
#    print('-------------')
