from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from pathResolver.models import ResolvedPath
from pathLogger.models import PathBlock
from pathResolver.serializers import ResolvedPathSerializer
from rest_framework import generics


class PathResolverView(APIView):
    def get(self, request):
        queryset = ResolvedPath.objects.impose()
        serializer = ResolvedPathSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PathResolverViewSafe(APIView):
    def get(self, request):
        queryset = ResolvedPath.objects.all()
        serializer = ResolvedPathSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


