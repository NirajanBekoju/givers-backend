from dataclasses import field
from pyexpat import model
from rest_framework import serializers


from .models import Events, LikeEvent
from customuser.models import User
from category.serializers import EventCategorySerializer


class LikeEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeEvent
        fields = ['user', 'date']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'admin']


class EventSerializer(serializers.ModelSerializer):
    # user and category overides the fields of Event model
    user = UserSerializer(read_only=True, many=False)
    category = EventCategorySerializer(read_only=True, many=False)
    # here source is the related_name in the foreign key event in model of LikeEvent
    liked = LikeEventSerializer(many=True, read_only=True, source='likeevent')

    class Meta:
        model = Events
        # fields = '__all__'
        fields = ['name', 'user', 'category', 'liked']

class EventupdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'

