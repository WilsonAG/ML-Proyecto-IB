from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
import datetime

from webapp.lib import tweets, emoticons, nlp, regresion as reg


def index(req):
    return render(req, 'home.html')


def analysis(req):
    num_tweets = req.GET['quantity']
    twts = ['🇪🇨ECUADOR🇪🇨 😷Casos: 46.356 ☠️Mortes: 3.874 🍀Curados: 22.865 ‼️Mortalidade: 8.4% 🧪Testes feitos: 134.141 #Coronavírus',
            'Amo mucho el maquillaje ♥️ que pensé hacer una sombra de unicornio 🦄 #unicornio #makeup #maquillaje #arte #coronavirus #CuarentenaExtendida #Ecuador #gay #LGBT #gaynegros https://t.co/Z75WMvIxyQ',
            '@MarcoAnibal La sociedad civil ecuatoriana esperando un reportaje de estos temas de la señora @tinocotania y ella en otra onda. #Bucaram #coronavirus #Ecuador #EcuadorEntérate #EresPoblacionDeAltoRiesgoSi',
            'Guayaquil fue ejemplo de la tragedia. Ahora ha logrado pasar de mas de 400 muertos diarios a ninguno. Ahora tambien deberíamos estar hablando de la gestión de esta ciudad. https://t.co/qCADbaloBe',
            '#Ecuador registra 3.874 muertes oficiales y 46.356 positivos por coronavirus https://t.co/2i27wF8tvU']

    # twts = tweets.get(int(num_tweets))
    cleaned = nlp.do_nlp(twts)

    good_dict = nlp.get_dictionary(True)
    bad_dict = nlp.get_dictionary(False)

    jaccard_tags = nlp.get_jaccard_tags(set(good_dict), set(bad_dict), twts)

    good_fii = nlp.get_fii(cleaned, good_dict)
    bad_fii = nlp.get_fii(cleaned, bad_dict)
    good = nlp.do_cosine_method(good_fii, good_dict, cleaned)
    bad = nlp.do_cosine_method(bad_fii, bad_dict, cleaned)

    cosine_tags = nlp.get_tags(good, bad, twts)

    cos_pos = nlp.get_percent(cosine_tags)
    cos_neg = nlp.get_percent(cosine_tags, False)

    jac_pos = nlp.get_percent(jaccard_tags)
    jac_neg = nlp.get_percent(jaccard_tags, False)

    params = {'jac_tags': jaccard_tags, 'cos_tags': cosine_tags,
              'cos_pos': cos_pos, 'cos_neg': cos_neg,
              'jac_pos': jac_pos, 'jac_neg': jac_neg}
    return render(req, 'home.html', params)


def regresion(req):
    train, test = reg.load_data('../data/tweets/tweets.csv')
    model = reg.eval(train, test)

    result = reg.test_model(model, train, test)

    result_html = str(reg.parse_html(result))

    meta = reg.error(result)

    return render(req, 'regresion.html', {'html': result_html, 'meta': meta})


def about(req):
    return render(req, 'about.html')
