import lib.nlp as nlp
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
def analizer(tweet):
    vs = analyzer.polarity_scores(tweet)
    print(vs)
    estado=" "
    value_pos=vs['pos']
    value_neg=vs['neg']
    if value_pos > value_neg:
        print(value_pos, " ", value_neg)
        estado='positivo'
    elif value_pos < value_neg:
            estado='negativo'
    else:
        estado='neutro'
    return estado
#tweet='eres el amor de mi vida gracias por compartir tantos bellos momentos juntos'
tweet='Coronavirus en Ecuador: asi hacen frente al coronavirus los indigenas de la Amazonia'
print(analizer(tweet))