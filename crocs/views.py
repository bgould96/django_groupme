from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

import requests, json

def index(request):
    test = request["response"];

    return HttpResponse("<p>" + test + "</p>");
