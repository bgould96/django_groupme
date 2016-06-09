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
        name = request.POST[0]["name"]
        sender_type = request.POST["sender_type"]

        f = open("/home/ubuntu/groupme/crocs/log.txt", "w")
        f.write(name + " CALLED BACK")
        f.close()

        if sender_type == "user":
                json_data = {"bot_id": "f6c64113661287ad36f855469a", "message": name}

                resp = requests.post(
                     "https://api.groupme.com/v3/bots/post",
                      data=json.dumps(json_data)
                )

        return HttpResponse("")