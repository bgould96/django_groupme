from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

import requests, json

required_ids = [""]

@csrf_exempt
def index(request):
        print request



        return HttpResponse("Users updated.")