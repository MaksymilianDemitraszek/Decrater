from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import DestroyAPIView,CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from pathResolver.models import ResolvedPath
from pathResolver.serializers import ResolvedPathSerializer, PathListSerializer

from pathLogger import serializers


class PathResolverView(APIView):
    def get(self, request)
        queryset = ResolvedPath.objects.impose()

        serializer = PathListSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)




