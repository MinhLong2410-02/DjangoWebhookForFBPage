from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
import os
from dotenv import load_dotenv
from .bot import *

load_dotenv("./.env")
PAGE_ACCESS_TOKEN = os.getenv("PAGE_ACCESS_TOKEN")
APP_SECRET = os.getenv("APP_SECRET")


# Create your views here.
class VerifyView(APIView):
    def get(self, request, *args, **kwargs):
        if request.GET.get("hub.mode") == "subscribe" and request.GET.get(
                "hub.challenge"):
            if not request.GET.get("hub.verify_token") == APP_SECRET:
                print(request.GET.get("hub.verify_token"))
                return HttpResponse("Verification token mismatch", status=403)
            return HttpResponse(request.GET["hub.challenge"], status=200)
        return HttpResponse("Hello world", status=200)

    def post(self, request, *args, **kwargs):
        data = request.data
        if data["object"] == "page":
            for entry in data["entry"]:
                for messaging_event in entry["messaging"]:
                    sender_id = messaging_event["sender"]["id"]
                    recipient_id = messaging_event["recipient"]["id"]
                    if messaging_event.get("message"):
                        if messaging_event["message"].get("text"):
                            message_text = messaging_event["message"]["text"]
                            send_message(sender_id, message_text)
        return HttpResponse("POST SUCESSFULLY", status=200)


class DeploymentView(APIView):
    def get(self, request, *args, **kwargs):
        return HttpResponse("DEPLOY SUCESSFULLY", status=200)
