from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
import datetime

from webapp.lib import tweets, emoticons, nlp


def index(req):
    return render(req, 'home.html')


def analysis(req):
    num_tweets = req.GET['quantity']
    twts = ['hola a todo el mundo em fue bien en gracias',
            'amo a todos que les avaya bien',

            'maldad en el mundo corrupcion y covid']
    # cleaned = nlp.do_nlp(twts)

    # good_dict = nlp.get_dictionary(True)
    # bad_dict = nlp.get_dictionary(False)

    # good_fii = nlp.get_fii(cleaned, good_dict)
    # bad_fii = nlp.get_fii(cleaned, bad_dict)
    # good = nlp.do_cosine_method(good_fii, good_dict, cleaned)
    # bad = nlp.do_cosine_method(bad_fii, bad_dict, cleaned)

    # print(bad)
    params = {'tweets': twts}
    return render(req, 'home.html', params)


def regresion(req):
    file = open('webapp/templates/regresion.html')
    page = Template(file.read())
    file.close()
    ctx = Context()
    response = page.render(ctx)
    return HttpResponse(response)


def about(req):
    return render(req, 'about.html')
