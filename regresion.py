import lib.nlp as nlp
import pandas as pd
import lib.emoticons as emo
import emoji
import random
from sklearn.model_selection import train_test_split 



if __name__ == "__main__":
    datac=pd.read_csv('./data/tweets/tweets.csv', encoding='utf-8')
    #datac=datac[0:5]
    # print(datac)
    data=nlp.do_nlp(datac['tweets'])
    sent=datac['status']
    sent=sent.values.tolist()
    sen=[]
    for i in sent:
        if i=='positivo':
            sen.append('+')
        else:
            sen.append('-')
        print(i)
    fii=nlp.get_fii(data,None,True)
    diccionario=[i[0] for i in fii]

    print(data)
    #to do 2 data set
    train,test=train_test_split(data,test_size = 0.30)
    print("Ejemplos usados para entrenar: ", len(train))
    print("Ejemplos usados para test: ", len(test))
    print(test)
    print('-------------------------------------------------------------------------------------------------------------------------')
    print(train)
    # matrix de coseno
    # regresion  toca analizar




    #coseno=nlp.do_cosine_method(fii,diccionario,data)
    #print(coseno)
    #print(sen)
    # for i in range(len(data)):
    #     print(data[i]," ",sent[i])
    