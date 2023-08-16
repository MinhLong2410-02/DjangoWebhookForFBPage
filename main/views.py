from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse
import os
from dotenv import load_dotenv
load_dotenv("./.env")
PAGE_ACCESS_TOKEN = os.getenv("PAGE_ACCESS_TOKEN")

# Create your views here.
class VerifyView(APIView):
    def get(self, request, *args, **kwargs):
        if request.GET.get("hub.mode") == "subscribe" and request.GET.get("hub.challenge"):
            if not request.GET.get("hub.verify_token") == PAGE_ACCESS_TOKEN:
                return HttpResponse("Verification token mismatch", status=403)
            return HttpResponse(request.GET["hub.challenge"], status=200)
        return HttpResponse("Hello world", status=200)