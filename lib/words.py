import pandas as pd
def good_words():
    file = open('../data/diccionary/buenas.txt', 'r') 
    text = file.read() 
    items = text.split(",")
    return items
def bad_words():
    file = open('../data/diccionary/malas.txt', 'r') 
    text = file.read() 
    items = text.split(",")
    return items
good=good_words()
bad= bad_words()
#print('------- buena spalabras ')
#print(good)
#print('------- buena spalabras ')
#print(bad)