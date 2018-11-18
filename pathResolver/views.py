from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from pathResolver.models import ResolvedPath
from pathResolver.serializers import ResolvedPathSerializer


class PathResolverView(APIView):
    def get(self, request):
        queryset = ResolvedPath.objects.impose()
        serializer = ResolvedPathSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)




