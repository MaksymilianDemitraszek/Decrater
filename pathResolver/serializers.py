from rest_framework import serializers
from pathResolver.models import ResolvedPath, ResolvedDelta
from pathLogger.serializers import QuakeDelta


class ResolvedPathSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResolvedPath
        fields = ('id', 'latStart', 'lngStart', 'latEnd', 'lngEnd', 'color')
