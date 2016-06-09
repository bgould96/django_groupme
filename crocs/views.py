from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

import requests, json

@csrf_exempt
def index(request):
    name = request["name"];

    f = open("/home/ubuntu/groupme/crocs/log.txt", "w")
    f.write("BOT CALLED BACK")
    f.close()

    return HttpResponse("");
