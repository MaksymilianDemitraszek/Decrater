from rest_framework import serializers
from pathLogger.models import PathBlock, QuakeEvent

class QuakeEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuakeEvent
        fields = ('x', 'y', 'z')


class PathBlockSerializer(serializers.ModelSerializer):
    quakeEvents = QuakeEventSerializer(many=True)
    class Meta:
        model = PathBlock
        fields = '__all__'

    def create(self, validated_data):
        path_data = validated_data.copy()
        if 'quakeEvents' in path_data:
            del path_data['quakeEvents']

        path_block = PathBlock.objects.create(**path_data)
        events_instances_list = self._get_event_instances_list(validated_data['quakeEvents'], path_block)
        events = QuakeEvent.objects.bulk_create(events_instances_list, )
        return path_block

    def _get_event_instances_list(self, event_data_list, parent_path):
        return [QuakeEvent(parent_path=parent_path, **event) for event in event_data_list]

