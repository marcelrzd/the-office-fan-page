from datetime import datetime
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, generics

import requests
from .models import *
from .serializers import *

# Fetch and save data from the office api into the database
class FetchAndSaveSeasons(APIView):
    def get(self, request):
        response = requests.get('https://theofficeapi.dev/api/seasons')
        data = response.json()

        for season in data:
            if not Season.objects.filter(id=season['id']):
                season_object = Season(
                    id=season['id'],
                    number=season['number'],
                    start_date=season['startDate'],
                    end_date=season['endDate'],
                )
                season_object.save()

        return Response(data)

class FetchAndSaveEpisodes(APIView):
    def get(self, request):
        response = requests.get('https://theofficeapi.dev/api/episodes?limit=201&includeCharacters=true')
        data = response.json()

        for episode in data['results']:
            if  not Episode.objects.filter(id=episode['id']):

                episode_object = Episode(
                    id=episode['id'],
                    title=episode['title'],
                    summary=episode['summary'],
                    air_date=episode['airDate'],
                    season_episode_number=episode['episode'],
                    series_episode_number=episode['seriesEpisodeNumber'],
                    season=Season.objects.filter(id=episode['seasonId']).first(),
                )
                episode_object.save()

                if episode['mainCharacters']:
                    for char in episode['mainCharacters']:
                        char_object = Character.objects.filter(id=char['id']).first()
                        if char_object:
                            episode_object.main_characters.add(char_object)
                    episode_object.save()
                if episode['supportingCharacters']:
                    for char in episode['supportingCharacters']:
                        char_object = Character.objects.filter(id=char['id']).first()
                        if char_object:
                            episode_object.supporting_characters.add(char_object)
                    episode_object.save()
                if episode['recurringCharacters']:
                    for char in episode['recurringCharacters']:
                        char_object = Character.objects.filter(id=char['id']).first()
                        if char_object:
                            episode_object.recurring_characters.add(char_object)
                    episode_object.save()
        
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
    
# Fetching data from database to list and filter in the frontend
class FetchSeasons(generics.ListAPIView):
    seasons = Season.objects.all()
    serializer = SeasonSerializer(seasons, many=True)

class FetchEpisodes(generics.ListAPIView):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer

class FetchCharacters(generics.ListAPIView):
    characters = Character.objects.all()
    serializer = CharacterSerializer



