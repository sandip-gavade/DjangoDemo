from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader


def testpaper(request):
    que = "Who developed Python?"
    a = "Dennis Ritchie"
    b = "Guindo Van Russom"
    c = "Ken Thomson"
    d = "Bijourne Stroustrup"
    context = {
        'que': que,
        'options': [a, b, c, d]
    }
    template = loader.get_template('testpaper.html')
    response = template.render(context, request)
    return HttpResponse(response)


def result(request):
    return HttpResponse("result")
