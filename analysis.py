import lib.nlp as nlp
import pandas as pd

if __name__ == "__main__":
    data = pd.read_excel('./data.xlsx', encoding='utf-8')
    index = 0
    docs=list(map(lambda x: str(x).strip(),data['tweets']))
    docs=list(map(nlp.clean,docs))
    docs=list(map(lambda x: x.split(),docs))
    docs=list(map(nlp.clean_stop_words,docs))
    docs=list(map(nlp.clean_stemmer,docs))
    fii=nlp.get_fii(docs)
    for i in fii:
        print(i[0])
