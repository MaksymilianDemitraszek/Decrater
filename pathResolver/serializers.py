from rest_framework import serializers
from pathResolver.models import ResolvedPath, ResolvedDelta
from pathLogger.serializers import QuakeDelta


class ResolvedPathSerializer(serializers.ModelSerializer):
    # deltas = QuakeDelta(many=True)
    avg_delta = serializers.SerializerMethodField()


    class Meta:
        model = ResolvedPath
        fields = ('id', 'latStart', 'lngStart', 'latEnd', 'lngEnd')

    def get_avg_delta(self):
        path = ResolvedPath.objects.get(id=self.id)
        return path.average_delta()

class PathListSerializer(serializers.Serializer):
    pathList = ResolvedPathSerializer(read_only=True, many=True)




