import os
import pytweet
import time

client=pytweet.Client(os.environ["bearer_token"], consumer_key=os.environ["api_key"], consumer_key_secret=os.environ["api_key_secret"], access_token=os.environ["access_token"], access_token_secret=os.environ["access_token_secret"])


tweet=client.tweet("Tweet... tweet... 🐦")
print(tweet)
print(f"Done, check it please uwu")