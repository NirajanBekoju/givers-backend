from django.db.models import fields
from rest_framework import serializers

from .models import requestevents

class requesteventSerializervolunteer(serializers.ModelSerializer):
    class Meta:
        model=requestevents
        fields=['user','event','description','interested','request_volunteer','user_details']

class approvalSerializer(serializers.ModelSerializer):
    class Meta:
        model=requestevents
        fields='__all__'