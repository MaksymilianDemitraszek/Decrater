from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView,CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from . import models

from pathLogger import serializers

class PathLoggerView(APIView):
    def post(self, request):

        text_file = open("Output.txt", "w")
        text_file.write(str(request.data))
        text_file.close()

        serializer = serializers.PathBlockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)

