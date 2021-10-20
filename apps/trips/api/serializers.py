from django.db.models import fields
from rest_framework import serializers

from apps.trips.models import Passanger, Travel

class TravelApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Travel
        fields = '__all__'

class PassangerApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Passanger
        fields = '__all__'