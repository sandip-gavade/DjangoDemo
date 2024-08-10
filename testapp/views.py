from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


# Create your views here.


def greetings(request):
    return HttpResponse("Hello From First View page")


def about(request):
    text = "sandip"
    template = loader.get_template('about.html')
    context = {'text': text}
    response = template.render(context, request)
    return HttpResponse(response)


def contact(request):
    return HttpResponse("Contact Page")
