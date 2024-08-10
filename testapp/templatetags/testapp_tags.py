import datetime
from django import template

register = template.Library()


@register.simple_tag(name="today")
def getdate():
    n = datetime.datetime.now()
    return n


@register.filter
def quote(value):
    s = '"' + str(value) + '"'
    return s
