from rest_framework import serializers

from apps.destinations.models import Destination

class DestinationApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = 'id', 'name', 'available', 'price'
