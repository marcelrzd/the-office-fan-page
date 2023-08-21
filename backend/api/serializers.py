# serializers.py

from datetime import datetime
from rest_framework import serializers
from .models import *


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Season
        fields = '__all__'


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'


class EpisodeSerializer(serializers.ModelSerializer):
    season_number = serializers.SerializerMethodField()
    main_characters = serializers.SerializerMethodField()
    recurring_characters = serializers.SerializerMethodField()
    supporting_characters = serializers.SerializerMethodField()

    class Meta:
        model = Episode
        fields = '__all__'

    def get_season_number(self, obj):
        return obj.season.number

    def get_main_characters(self, obj):
        chars = obj.main_characters.all()
        return [{'id': char.id, 'name': char.name} for char in chars]

    def get_recurring_characters(self, obj):
        chars = obj.recurring_characters.all()
        return [{'id': char.id, 'name': char.name} for char in chars]

    def get_supporting_characters(self, obj):
        chars = obj.supporting_characters.all()
        return [{'id': char.id, 'name': char.name} for char in chars]


class RandomQuoteSerializer(serializers.ModelSerializer):
    character = serializers.SerializerMethodField()

    class Meta:
        model = Quote
        fields = ['character', 'quote']

    def get_character(self, obj):
        char = obj.character
        if char:
            return ({'name': char.name})
        else:
            return None
