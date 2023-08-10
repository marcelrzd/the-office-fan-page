from datetime import datetime
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from .models import Season
from .serializers import SeasonSerializer

class FetchAndSaveSeasons(APIView):
    def get(self, request):
        response = requests.get('https://theofficeapi.dev/api/seasons')
        data = response.json()

        for season in data:
            season_object = Season(
                number=season['number'],
                start_date=season['startDate'],
                end_date=season['endDate'],
            )
            season_object.save()

        return Response(data)
