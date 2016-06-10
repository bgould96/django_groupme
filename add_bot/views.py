#!/usr/bin/env python3

from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

import requests, json

required_ids = [""]

@csrf_exempt
def index(request):
        resp = requests.get("https://api.groupme.com/v3/groups/21514110?token=b1580fb0ec9401334a16001f5a739d7d")

        pyth_obj = json.loads(resp.text)

        f = open("/home/ubuntu/groupme/add_bot/log.txt", "w")
        f.write(resp.text)
        f.close()

        for chk_id in required_ids:
                found = False

                for member in pyth_obj["response"]["members"]:
                        if member["user_id"] == chk_id:
                                found = True

                if found == False:
                        json_data = {"members":[{"nickname": "Jon", "user_id": chk_id}]}

                        resp = requests.post(
                                "https://api.groupme.com/v3/groups/21514110/members/add?token=b1580fb0ec9401334a16001f5a739d7d",
                                data=json.dumps(json_data)
                        )



        return HttpResponse("Users updated.")

@csrf_exempt
def crocs(request):
        json_data = {"bot_id": "816fc2dbe8c8af12dfb3c920a3", "message": "Croc Fact Here"}

        resp = requests.post(
                "https://api.groupme.com/v3/bots/post",
                data=json.dumps(json_data)
        )

        return HttpResponse("")