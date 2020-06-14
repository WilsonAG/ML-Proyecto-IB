import lib.nlp as nlp
import pandas as pd
import lib.emoticons as emo
import numpy as np
import emoji
import random
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from bs4 import BeautifulSoup


def status(sent):
    sen = []
    for i in sent:
        if i == 'positivo':
            sen.append(1)
        else:
            sen.append(0)
    return sen


def error(result, origin):
    cont = 0
    size = len(result)
    for i in range(size):

        if predictions[i] == te_sen[i]:
            cont += 0
        else:
            cont += 1
    erro = (cont*len(predictions))/100
    print("el porcentaje de error es de ", erro, " %")
    return erro


def load_data(path):
    data = pd.read_csv(path, encoding='utf-8')
    train, test = train_test_split(data, test_size=0.30)
    return train, test


def eval(train, test):
    tr_sen = status(train['status'])
    train_nlp = nlp.do_nlp(train['tweets'])
    test_nlp = nlp.do_nlp(test['tweets'])
    con = 0
    doc = train_nlp+test_nlp
    diccionary = nlp.get_dict(doc)
    fii = nlp.get_fii(train_nlp, diccionary)
    tb_wtf = nlp.get_tf_word_bag(fii, diccionary, train_nlp, True)
    tb_tf = nlp.get_tf_word_bag(fii, diccionary, train_nlp, False)
    idf = nlp.get_df_idf(diccionary, tb_tf, tb_wtf, True)
    tf_idf = nlp.get_mtx_tf_idf(diccionary, train_nlp, tb_wtf, idf)
    # print(tf_idf)
    tf_idf = tf_idf.T
    tf_idf['status'] = tr_sen
    # print(tf_idf)
    # regresion logistica trading
    X = np.array(tf_idf.drop(['status'], 1))
    y = np.array(tf_idf['status'])
    model = linear_model.LogisticRegression()
    model.fit(X, y)
    return model


def parse_html(result):
    soup = BeautifulSoup(result[0:10].to_html(
        classes=['table', 'table-hover'], border=0),
        'html5lib')
    soup.find('thead')['class'] = 'thead-dark'

    return soup.find('table')


def test_model(model, train, test):
    train_nlp = nlp.do_nlp(train['tweets'])
    test_nlp = nlp.do_nlp(test['tweets'])
    doc = train_nlp+test_nlp

    diccionary = nlp.get_dict(doc)

    # regresion logistica test
    tfii = nlp.get_fii(test_nlp, diccionary)
    ttb_wtf = nlp.get_tf_word_bag(tfii, diccionary, test_nlp, True)
    ttb_tf = nlp.get_tf_word_bag(tfii, diccionary, test_nlp, False)
    t_idf = nlp.get_df_idf(diccionary, ttb_tf, ttb_wtf, True)
    ttf_idf = nlp.get_mtx_tf_idf(diccionary, test_nlp, ttb_wtf, t_idf)
    ttf_idf = ttf_idf.T
    tX = np.array(ttf_idf)
    tweet = []
    for i in test_nlp:
        tweet.append(" ".join(i))
    te_sen = status(test['status'])
    predictions = model.predict(tX)
    result = pd.DataFrame(
        {'tweets': tweet, 'regresion': predictions, 'original': te_sen})

    return result
    # error(predictions, te_sen)

    # if __name__ == "__main__":
    #     datac = pd.read_csv('./data/tweets/tweets.csv', encoding='utf-8')

    #     train, test = train_test_split(datac, test_size=0.30)

    #     # 0 = negativo
    #     # 1 = positivo
    #     tr_sen = status(train['status'])
    #     train_nlp = nlp.do_nlp(train['tweets'])
    #     test_nlp = nlp.do_nlp(test['tweets'])
    #     con = 0
    #     doc = train_nlp+test_nlp
    #     diccionary = nlp.get_dict(doc)
    #     fii = nlp.get_fii(train_nlp, diccionary)
    #     tb_wtf = nlp.get_tf_word_bag(fii, diccionary, train_nlp, True)
    #     tb_tf = nlp.get_tf_word_bag(fii, diccionary, train_nlp, False)
    #     idf = nlp.get_df_idf(diccionary, tb_tf, tb_wtf, True)
    #     tf_idf = nlp.get_mtx_tf_idf(diccionary, train_nlp, tb_wtf, idf)
    #     # print(tf_idf)
    #     tf_idf = tf_idf.T
    #     tf_idf['status'] = tr_sen
    #     # print(tf_idf)
    #     # regresion logistica trading
    #     X = np.array(tf_idf.drop(['status'], 1))
    #     y = np.array(tf_idf['status'])
    #     model = linear_model.LogisticRegression()
    #     model.fit(X, y)
    #     # regresion logistica test
    #     tfii = nlp.get_fii(test_nlp, diccionary)
    #     ttb_wtf = nlp.get_tf_word_bag(tfii, diccionary, test_nlp, True)
    #     ttb_tf = nlp.get_tf_word_bag(tfii, diccionary, test_nlp, False)
    #     t_idf = nlp.get_df_idf(diccionary, ttb_tf, ttb_wtf, True)
    #     ttf_idf = nlp.get_mtx_tf_idf(diccionary, test_nlp, ttb_wtf, idf)
    #     ttf_idf = ttf_idf.T
    #     tX = np.array(ttf_idf)
    #     tweet = []
    #     for i in test_nlp:
    #         tweet.append(" ".join(i))
    #     te_sen = status(test['status'])
    #     predictions = model.predict(tX)
    #     result = pd.DataFrame(
    #         {'tweets': tweet, 'regresion': predictions, 'original': te_sen})
    #     print(result)
    #     error(predictions, te_sen)
