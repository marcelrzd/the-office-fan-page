# serializers.py

from datetime import datetime
from rest_framework import serializers
from .models import Season

class SeasonSerializer(serializers.ModelSerializer):
    start_date = serializers.DateField(source='startDate')
    end_date = serializers.DateField(source='endDate')

    class Meta:
        model = Season
        fields = '__all__'
        read_only_fields = ('id',)

    