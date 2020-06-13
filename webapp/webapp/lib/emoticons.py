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


def get_emojis(good=False):
    if good:
        doc = '../data/emojis/good_emojis.json'
    else:
        doc = '../data/emojis/bad_emojis.json'

    emoticon = open(doc, 'r')
    emoticon = json.load(emoticon)
    emotico = []
    for i in emoticon:
        emotico.append(emoji.emojize(i, use_aliases=True))
    return emotico


# good_emoji=open('data/emojis/good_emojis.json','r')
# bad_emoji=open('data/emojis/bad_emojis.json','r')
# good_emoji =json.load(good_emoji)
# bad_emoji =json.load(bad_emoji)

# for i in good_emoji:
#     print(emoji.emojize(i,use_aliases=True))


# '''
# devolver buenos y malos pero los emojis echos iconos con el emojize
# '''
