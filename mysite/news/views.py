from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    """ Контроллер-фукнция """
    print(request)
    return HttpResponse('Number one')


def test(request):
    print(dir(request))
    return HttpResponse('<b>Тестовая страница</b>')
