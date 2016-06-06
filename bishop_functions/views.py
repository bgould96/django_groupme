from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

import requests, json

required_ids = [""]

@csrf_exempt
def index(request):
        #id = request["name"]

        f = open("/home/ubuntu/groupme/bishop_functions/log.txt", "w")
        f.write("TEST")
        f.close()

        if id != "bishop_functions":
            msg = id + " sent a message."
            json_data = {"bot_id": "f6c64113661287ad36f855469a", "message": msg}

            resp = requests.post(
                    "https://api.groupme.com/v3/bots/post",
                    data=json.dumps(json_data)
            )

        return HttpResponse(request)