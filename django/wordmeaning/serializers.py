from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class wordsSerializer(serializers.ModelSerializer):
     class Meta:
         model = words
         fields = ('__all__')

