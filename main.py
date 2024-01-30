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

media = client.upload_media(filename='/Users/tharunteja/Downloads/Pushpa_ The Rule - Part 2 (2024)_files/MV5BZTQ3M2QxMTAtMmQ0Yi00YmVmLThkZGYtODBiN2NhNjBhYzcwXkEyXkFqcGdeQXVyMTY0MTg5OTM4._V1_.jpg')

days = date(2024,8,16) - date.today() - timedelta(days = 1)
cd = str(days.days) + " Days left for #Pushpa2TheRule Rampage \n\n@alluarjun"
response = client.create_tweet(text=cd, media_ids=[media.media_key])
