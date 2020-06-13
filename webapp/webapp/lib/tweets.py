import tweepy
import json
import pandas as pd


def get(quantity):
    consumer_key = "smVoKep6XDkxV6hr5cGltY47C"

    consumer_secret = "QXWh8Qr0hH2nWXiQYm2zoOe1RwkSBEAqDDu7w66uguoKeVQIgm"
    access_token = "1264729708379455491-jAdk8btCduTt1EYjzI8C5tomajjtUJ"
    access_token_secret = "qC0wH3b6RS5X5TEQNSUSV6O9hoyjaYO8EXnDePriAztuf"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth, wait_on_rate_limit=True,
                     wait_on_rate_limit_notify=True)
    twts = tweepy.Cursor(api.search, q='coronavirus ecuador -filter:retweets',
                         lang='es', tweet_mode='extended', geo_code="-1.39459,-78.39924", since='2020-06-05').items(quantity)

    my_tweets = []
    for tw in twts:
        text = tw._json['full_text']
        if text not in my_tweets:
            my_tweets.append(text)
    return my_tweets
