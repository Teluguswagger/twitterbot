import tweepy
import os
from datetime import date
from datetime import timedelta
from json import dumps

consumer_key = os.environ['API_KEY']
consumer_secret = os.environ['API_SECRET']
access_token = os.environ['ACCESS_TOKEN']
access_token_secret = os.environ['ACCESS_TOKEN_SECRET']

client = tweepy.Client(consumer_key=consumer_key,
                    consumer_secret=consumer_secret,
                    access_token=access_token,
                    access_token_secret=access_token_secret)

days = date(2024,12,06) - date.today() - timedelta(days = 1)
cd = str(days.days) + " Days left for #Pushpa2TheRule Rampage \n\n@alluarjun"
response = client.create_tweet(text=cd)
