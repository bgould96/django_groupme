from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

import requests, json

def index(request):
    return HttpResponse("<p>" + request + "</p>");
