from datetime import datetime
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests
from .models import *
from .serializers import SeasonSerializer

class FetchAndSaveSeasons(APIView):
    def get(self, request):
        response = requests.get('https://theofficeapi.dev/api/seasons')
        data = response.json()

        for season in data:
            season_object = Season(
                id=season['id'],
                number=season['number'],
                start_date=season['startDate'],
                end_date=season['endDate'],
            )
            season_object.save()

        return Response(data)


class FetchAndSaveCharacters(APIView):
    def get(self, request):
        response = requests.get('https://theofficeapi.dev/api/characters?limit=100')
        data = response.json()

        for character in data['results']:
            if not Character.objects.filter(id=character['id']):
                character_object = Character(
                    id=character['id'],
                    name=character['name'],
                    gender=character['gender'],
                    marital=character['marital'],
                    job=character['job'],
                    workplace=character['workplace'],
                    first_appearance=character['firstAppearance'],
                    last_appearance=character['lastAppearance'],
                    actor=character['actor'],
                )
                character_object.save()

        return Response(data)