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

    docs = nlp.do_nlp(data['tweets'])

    good = nlp.get_dictionary(True)
    bad = nlp.get_dictionary(False)

    docs = docs[0:20]
    good_fii = nlp.get_fii(docs, good)
    bad_fii = nlp.get_fii(docs, bad)
    docs = list(map(nlp.to_string, docs))
    resp = nlp.do_cosine_method(good_fii, good, docs)  #
    print(resp)
