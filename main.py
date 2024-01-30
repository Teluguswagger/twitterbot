import tweepy
import os
from datetime import date
from datetime import timedelta
from json import dumps

api_key = "Dcy5qVhM6BoWzSqUm4eC3eD9P"
api_secret = "HI1qANYmgpYtp6NE3gAyreOh3v1rkIMTQPKtiSzZLmBBEDc1ny"
bearer_token = "AAAAAAAAAAAAAAAAAAAAACKOsAEAAAAALhaVx5HYqctmec6kTyvUI6ZhZTM%3Dp4fj4HdFUyLOqkz3dODmfIeE2kYuVTPJN01CiPSiTemSUdu7yr"
access_token = "1751968878341885952-FwHZorPORJNugpZ2lJNOQVGxBHBQsO"
access_token_secret = "92WuEA3u0SLlK9sokDN7WOLHKrnJ5NrA8BShMGK9S3LB2"
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)
auth = tweepy .OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

days = date(2024,8,15) - date.today() - timedelta(days = 1)
cd = str(days.days) + " Days left for #Pushpa2TheRule Rampage \n@alluarjun"
response = client.create_tweet(text=cd)
