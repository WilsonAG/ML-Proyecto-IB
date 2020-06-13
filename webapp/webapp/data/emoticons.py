import emoji
import json

bad_emojis = open('data/emojis/bad_emojis.json', 'r')
bad_emojis = json.load(bad_emojis)

for i in bad_emojis:
    print(i)
