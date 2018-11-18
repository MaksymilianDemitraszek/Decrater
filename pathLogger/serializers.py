from rest_framework import serializers
from pathLogger.models import PathBlock, QuakeDelta


class QuakeEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuakeDelta
        fields = ('x', 'y', 'z')


class PathBlockSerializer(serializers.ModelSerializer):
    quakeEvents = QuakeEventSerializer(many=True, required=False)

    class Meta:
        model = PathBlock
        fields = '__all__'
        extra_kwargs = {
            'quakeDelta': {'read_only': True}
        }

    def create(self, validated_data):
        path_block_data, quake_events = self._split_to_paht_and_events(**validated_data)
        delta = QuakeDelta.objects.create_delta_from_event_list(path_block_data['deviceId'], quake_events,)
        path_block = PathBlock.objects.create(quakeDelta=delta, **path_block_data)
        return path_block

    def _get_event_instances_list(self, event_data_list, parent_path):
        return [QuakeDelta(parent_path=parent_path, **event) for event in event_data_list]

    def _split_to_paht_and_events(self, **validated_data):
        path_data = validated_data.copy()
        if 'quakeEvents' in path_data:
            del path_data['quakeEvents']
        return path_data, validated_data['quakeEvents']
