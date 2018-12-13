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


consumer_key = ' '
consumer_secret = ''
access_token = ''
access_secret = ''
# 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
auth_api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

# Open/Create a file to append data
#user_input = input("Enter the path of your file: ")
#df = pd.read_csv(user_input)
with open('brand24.csv','a') as f:

    
 #Use csv Writer
 csvWriter = csv.writer(f)
 csvWriter.writerow(['Account name', 'Date Tweeted', 'Tweet','Media url'])
 while True: 
     account = input('Enter the account name that you want to stream (without \'@\'). Enter \'exit\' to stop: ' )
     
     if account != 'exit':
        #for target in account_list:
        print("Getting data for " + account)
        item = auth_api.get_user(account)
        print("name: " + item.name)
        print("screen_name: " + item.screen_name)
        print("description: " + item.description)
        print("statuses_count: " + str(item.statuses_count))
        print("friends_count: " + str(item.friends_count))
        print("followers_count: " + str(item.followers_count))
        
        #tweet_count = 0
        #end_date = datetime.utcnow() - timedelta(days=186)
        
        end_date = datetime.strptime('Apr 1 2018  1:00AM', '%b %d %Y %I:%M%p')
        print(end_date)
        for status in Cursor(auth_api.user_timeline, id=account).items():
         #tweet_count += 1
         media_url = ''
         media = status.entities.get('media', [])
         if(len(media) > 0):
             media_url = media[0]['media_url']
             
         if(account != 'Charles_SEO' and account != 'brightonseo' and account != 'anton_shulke' and account != 'semrush'):
             if (not status.retweeted) or ('RT @' not in status.text):
                 csvWriter.writerow([status.user.screen_name, status.created_at,status.text.encode('utf-8'),media_url])
   
    
         if status.created_at < end_date:
            break
    
     if account == 'exit':
        break
    
 f.close()
     

