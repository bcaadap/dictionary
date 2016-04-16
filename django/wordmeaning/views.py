
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import words
from .serializers import wordsSerializer
from django.http import request
# Create your views here.
@api_view(['GET','POST'])
def word_list(request):
    if request.method == 'GET':
        try:
            getData=words.objects.get(word=request.data['word'])
            serializer = wordsSerializer(getData)
            return Response(serializer.data)
        except:
            return Response("not found", status = status.HTTP_400_BAD_REQUEST)
    elif request.method == 'POST':
        serializer = wordsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

