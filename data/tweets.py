import tweepy
import json
import pandas as pd

consumer_key = "smVoKep6XDkxV6hr5cGltY47C"
consumer_secret = "QXWh8Qr0hH2nWXiQYm2zoOe1RwkSBEAqDDu7w66uguoKeVQIgm"
access_token = "1264729708379455491-jAdk8btCduTt1EYjzI8C5tomajjtUJ"
access_token_secret = "qC0wH3b6RS5X5TEQNSUSV6O9hoyjaYO8EXnDePriAztuf"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# tweets = api.search(q="coronavirus", tweet_mode='extended', lang='es')
tweets = tweepy.Cursor(api.search, q='coronavirus ecuador -filter:retweets',
                       lang='es', tweet_mode='extended', geo_code="-1.39459,-78.39924", since='2020-06-05').items(500)

my_tweets = []
for tw in tweets:
    text = tw._json['full_text']
    if text not in my_tweets:
        my_tweets.append(text)
    # print(json.dumps(tw._json, indent=4))

data = pd.DataFrame(my_tweets, columns=['tweets'])

with pd.ExcelWriter('tweets.xlsx') as writer:
    data.to_excel(writer, index=False)
