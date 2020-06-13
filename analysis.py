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
    data1 = data['tweets'].tolist()[0:20]

    docs = nlp.do_nlp(data['tweets'])

    good = nlp.get_dictionary(True)
    bad = nlp.get_dictionary(False)

    docs = docs[0:20]
    tags_j = nlp.get_jaccard_tags(set(good), set(bad), data1)
    print(tags_j)
    # Cosine
    # good_fii = nlp.get_fii(docs, good)
    # bad_fii = nlp.get_fii(docs, bad)
    # good = nlp.do_cosine_method(good_fii, good, docs)  #
    # bad = nlp.do_cosine_method(bad_fii, bad, docs)  #
    # tags = nlp.get_tags(good, bad, data1)
    # for i in tags:
    #     print(i, tags[i])
