import lib.nlp as nlp
import pandas as pd
import lib.emoticons as emo
import emoji

def get_dictionary(doc):
    f=open(doc,encoding='utf-8')
    dictionary=[]
    for i in f:
        dictionary.append(i)
    dictionary=list(map(nlp.clean,dictionary))
    dictionary=list(map(lambda x: x.split(),dictionary))
    dictionary=list(map(nlp.clean_stemmer,dictionary))
    dictionary=list(map(lambda x: " ".join(x),dictionary))
    return list(set(dictionary))

def get_jaccard(query, document):
    interseccion = len(query.intersection(document))
    union = len(query.union(document))
    return interseccion / union

    



if __name__ == "__main__":
    data = pd.read_excel('./data.xlsx', encoding='utf-8')
    good='./data/new/buenas.txt'
    bad='./data/new/mala.txt'
    good_emoticon='data/emojis/good_emojis.json'
    bad_emoticon='data/emojis/bad_emojis.json'

    index = 0
    docs=list(map(lambda x: str(x).strip(),data['tweets']))
    docs=list(map(nlp.clean,docs))
    #print(docs[806])
    docs=list(map(lambda x: x.split(),docs))
    docs=list(map(nlp.clean_stop_words,docs))
    docs=list(map(nlp.clean_stemmer,docs))
    # fii=nlp.get_fii(docs)

    good=get_dictionary(good)
    bad=get_dictionary(bad)
    good_emoticon=emo.get_emojis(good_emoticon)
    bad_emoticon=emo.get_emojis(bad_emoticon)
    good+=good_emoticon
    bad+=bad_emoticon
    print(len(good))
    print(len(bad))
    
    
    # doc=docs[806]
    # print(doc)
    
    # more=get_jaccard(set(good),set(doc))
    # low=get_jaccard(set(bad),set(doc))


