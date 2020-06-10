import pandas as pd
import json 
import emoji

def good_words():
    file = open('./data/diccionary/buenas.txt', 'r')
    text = file.read()
    items = text.split(",")
    return items


def bad_words():
    file = open('./data/diccionary/malas.txt', 'r')
    text = file.read()
    items = text.split(",")
    return items


#good = good_words()
#bad = bad_words()
#for i in good:
#    print(i)
#print('------- buena spalabras ')
# print(good)
#print('------- buena spalabras ')
# print(bad)

good_emoji=open('data\emojis\good_emojis.json','r')
good_emoji =json.load(good_emoji)

for i in good_emoji:
    print(emoji.emojize(i,use_aliases=True))


