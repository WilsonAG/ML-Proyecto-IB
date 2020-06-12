import lib.nlp as nlp
import pandas as pd
import lib.emoticons as emo
import emoji
import random

def get_etiquetado(more, low):
    if more > low:
        return "Positivo"
    elif low > more:
        return "Negativo"
    else:
        return "Neutro"


if __name__ == "__main__":
    data = pd.read_excel('./data.xlsx', encoding='utf-8')
    good = './data/diccionary/buenas.txt'
    bad = './data/diccionary/malas.txt'
    good_emoticon = 'data/emojis/good_emojis.json'
    bad_emoticon = 'data/emojis/bad_emojis.json'


    docs=nlp.do_nlp(data['tweets'])
    # docs = list(map(lambda x: str(x).strip(), data['tweets']))
    # docs = list(map(nlp.clean, docs))
    # docs = list(map(lambda x: x.split(), docs))
    # docs = list(map(nlp.clean_stop_words, docs))
    # docs = list(map(nlp.clean_stemmer, docs))

    good = nlp.get_dictionary(good)
    bad = nlp.get_dictionary(bad)
    good_emoticon = emo.get_emojis(good_emoticon)
    bad_emoticon = emo.get_emojis(bad_emoticon)
    good += good_emoticon
    bad += bad_emoticon

    # print(len(bad)-len(good))

    # doc = docs[random.randrange(len(docs))]
    # print(doc)

    # more = nlp.get_jaccard(set(good), set(doc))
    # low = nlp.get_jaccard(set(bad), set(doc))
    # etiqueta = get_etiquetado(more, low)
    # print(etiqueta)
    # #docs=list(map(lambda x : " ".join(x),docs))
    
    docs=docs[0:20]
    good_fii = nlp.get_fii(docs, good,False)
    bad_fii = nlp.get_fii(docs, bad,False)
    docs = list(map(nlp.to_string, docs))
    resp=nlp.do_cosine_method(good_fii, good, docs)
    print(resp)
