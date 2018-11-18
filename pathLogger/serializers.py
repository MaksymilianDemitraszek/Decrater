from rest_framework import serializers
from pathLogger.models import PathBlock, QuakeDelta, PathCell
import json, base64


class QuakeEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuakeDelta
        fields = ('x', 'y', 'z')


class PathBlockSerializer(serializers.ModelSerializer):
    quakeEvents = serializers.CharField()

    class Meta:
        model = PathBlock
        fields = '__all__'
        extra_kwargs = {
            'quakeDelta': {'read_only': True}
        }

    def create(self, validated_data):
        path_block_data, quake_events = self._split_to_paht_and_events(**validated_data)

        quake_events = quake_events.rstrip()
        quake_events = json.loads(base64.b64decode(quake_events))




    def _get_event_instances_list(self, event_data_list, parent_path):
        return [QuakeDelta(parent_path=parent_path, **event) for event in event_data_list]

    def _split_to_paht_and_events(self, **validated_data):
        path_data = validated_data.copy()
        if 'quakeEvents' in path_data:
            del path_data['quakeEvents']
        return path_data, validated_data['quakeEvents']

class PathCellSerializer(serializers.ModelSerializer):
    start = serializers.BooleanField(required=False)
    end = serializers.BooleanField(required=False)
    packageId = serializers.IntegerField(required=True)

    class Meta:
        model = PathCell
        fields = '__all__'

    def create(self, validated_data):
        merge = False
        if 'start' in validated_data:
            del validated_data['start']
        if 'end' in validated_data:
            if validated_data['end'] == True:
                merge = True
            del validated_data['end']
        cell =PathCell.objects.create(**validated_data)

        if merge: self.merge(validated_data)

        return cell
    def merge(self, validated_data):
        cells = PathCell.objects.filter(packageId=validated_data['packageId'])
        quake_events = []
        for cell in cells:
            quake_events.append(
                {
                    "x": cell.x,
                    "y": cell.y,
                    "z": cell.z,
                }
            )
        first = cells[0]
        last = cells[len(cells)-1]
        delta = QuakeDelta.objects.create_delta_from_event_list(first.deviceId, quake_events,)
        path_block = PathBlock.objects.create(
            quakeDelta=delta,
            deviceId=first.deviceId,
            timestampStart = first.timestamp,
            timestampEnd = last.timestamp,
            latStart = first.lat,
            lngStart = first.lng,
            latEnd = last.lat,
            lngEnd = last.lng,
                                              )
        return path_block

