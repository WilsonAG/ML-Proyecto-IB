from django.http import HttpResponse
from django.template import Template, Context
import datetime


def index(req):
    home_template = open('webapp/templates/home.html')
    home = Template(home_template.read())
    home_template.close()
    ctx = Context({"name": "Will"})
    response = home.render(ctx)
    return HttpResponse(response)


def regresion(req):
    file = open('webapp/templates/regresion.html')
    page = Template(file.read())
    file.close()
    ctx = Context()
    response = page.render(ctx)
    return HttpResponse(response)
