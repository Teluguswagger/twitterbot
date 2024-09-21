import tweepy
import os
from datetime import date, datetime
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

# Event date
event_date = date(2024, 12, 6)

# Current date
today = date.today()

# Total number of days between today and event date
total_days = (event_date - today).days

# Event duration (adjustable)
start_date = date(2024, 9, 1)  # Example start date for the countdown
elapsed_days = (today - start_date).days

# Calculate the percentage of time passed
if total_days > 0:
    progress_percentage = (elapsed_days / (elapsed_days + total_days)) * 100
else:
    progress_percentage = 100  # Event has already passed

# Create a progress bar
progress_bar_length = 20  # Length of the progress bar (number of characters)
filled_length = int(progress_bar_length * (progress_percentage / 100))
bar = '▓' * filled_length + '░' * (progress_bar_length - filled_length)

# Status message with line gap before the progress bar
if total_days > 0:
    status = (f"{total_days} Days left for #Pushpa2TheRule Rampage\n\n"
              f"[{bar}] {progress_percentage:.0f}%")
elif total_days == 0:
    status = "Today is the day! #Pushpa2TheRule Rampage begins! @alluarjun"
else:
    status = f"{abs(total_days)} days since #Pushpa2TheRule Rampage @alluarjun\n\n[{bar}] {progress_percentage:.0f}%"

# Tweet the status
response = client.create_tweet(text=status)
