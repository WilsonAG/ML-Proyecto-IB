import lib.nlp as nlp
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def analize(tweet):
    analyzer = SentimentIntensityAnalyzer()
    vs = analyzer.polarity_scores(tweet)
    estado = " "
    value_pos = vs['pos']
    value_neg = vs['neg']
    if value_pos > value_neg:
        estado = 'positivo'
    elif value_pos < value_neg:
        estado = 'negativo'
    else:
        estado = 'neutro'
    return estado
