import lib.nlp as nlp
import pandas as pd

def get_dictionary(doc):
    f=open(doc)
    dictionary=[]
    for i in f:
        dictionary.append(str(i))
    dictionary=list(map(nlp.clean,dictionary))
    dictionary=list(map(lambda x: x.split(),dictionary))
    dictionary=list(map(nlp.clean_stemmer,dictionary))
    dictionary=list(map(lambda x: " ".join(x),dictionary))
    return dictionary



if __name__ == "__main__":
    data = pd.read_excel('./data.xlsx', encoding='utf-8')
    good='./data/new/buenas.txt'
    bad='./data/new/mala.txt'
    
    index = 0
    docs=list(map(lambda x: str(x).strip(),data['tweets']))
    docs=list(map(nlp.clean,docs))
    docs=list(map(lambda x: x.split(),docs))
    docs=list(map(nlp.clean_stop_words,docs))
    docs=list(map(nlp.clean_stemmer,docs))
    fii=nlp.get_fii(docs)
    
    good=get_dictionary(good)
    bad=get_dictionary(bad)
    print(bad)
    print(len(bad))

