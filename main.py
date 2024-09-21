

import tweepy
import os
from datetime import date
from datetime import timedelta
from json import dumps
from PIL import Image, ImageDraw, ImageFont

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
today = date.today()
total_days = (event_date - today).days

# Event duration (adjustable)
start_date = date(2024, 9, 1)
elapsed_days = (today - start_date).days

# Calculate progress percentage
if total_days > 0:
    progress_percentage = (elapsed_days / (elapsed_days + total_days)) * 100
else:
    progress_percentage = 100

# Image size and bar details
img_width, img_height = 400, 100
bar_width = 300
bar_height = 20
filled_length = int(bar_width * (progress_percentage / 100))

# Create an image with a white background
img = Image.new('RGB', (img_width, img_height), color = 'white')
draw = ImageDraw.Draw(img)

# Load a font
try:
    font = ImageFont.truetype("arial.ttf", 20)  # You can change this to a path to your font
except IOError:
    font = ImageFont.load_default()

# Draw the text
text = f"{total_days} Days left for #Pushpa2TheRule Rampage"
draw.text((10, 10), text, font=font, fill="black")

# Draw the progress bar outline
draw.rectangle([50, 50, 50 + bar_width, 50 + bar_height], outline="black", width=2)

# Draw the filled portion of the progress bar
draw.rectangle([50, 50, 50 + filled_length, 50 + bar_height], fill="green")

# Save the image
img_path = "progress_bar.png"
img.save(img_path)

# Tweet with the image
media = client.media_upload(img_path)
status = f"{total_days} Days left for #Pushpa2TheRule Rampage @alluarjun"
response = client.create_tweet(text=status, media_ids=[media.media_id])

print("Tweet posted with image!")
