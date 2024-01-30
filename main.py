import tweepy
import os
from datetime import date
from datetime import timedelta
from json import dumps

api_key = "api_key"
api_secret = "api_secret"
bearer_token = "bearer_token"
access_token = "access_token"
access_token_secret = "access_token_secret"
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy .OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

days = date(2024,8,15) - date.today() - timedelta(days = 1)
cd = str(days.days) + " Days left for #Pushpa2TheRule Rampage @alluarjun "
response = client.create_tweet(text=cd)
