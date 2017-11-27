from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def home_view(request):
    """."""
    template = loader.get_template('imagersite/home.html')
    response_body = template.render()
    return HttpResponse(response_body)


def login_view(request):
    """."""
    template = loader.get_template('imagersite/login.html')
    response_body = template.render()
    return HttpResponse(response_body)


def logout_view(request):
    """."""
    template = loader.get_template('imagersite/logout.html')
    response_body = template.render()
    return HttpResponse(response_body)


def registration(request):
    """."""
    template = loader.get_template('imagersite/registration.html')
    response_body = template.render()
    return HttpResponse(response_body)