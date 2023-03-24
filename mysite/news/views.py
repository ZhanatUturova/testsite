from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # print(dir(request))
    return HttpResponse('hello world')


def test(request):
    # print(dir(request))
    return HttpResponse('<h1>тестовая страница</h1>')