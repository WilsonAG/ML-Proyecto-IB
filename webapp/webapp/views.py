from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
import datetime
from webapp.lib import tweets
from webapp.lib import emoticons


def index(req):
    home = get_template('home.html')
    # my_tweets = tweets.get(10)
    my_tweets = ['tw1', 'tw2']
    emo = emoticons.good_words()
    params = {'tweets': emo}
    response = home.render(params)
    return HttpResponse(response)


def regresion(req):
    file = open('webapp/templates/regresion.html')
    page = Template(file.read())
    file.close()
    ctx = Context()
    response = page.render(ctx)
    return HttpResponse(response)
