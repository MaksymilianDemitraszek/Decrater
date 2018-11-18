from django.db import models

# Create your models here.
from django.db import models
from django.db.models import Q, Max

class PathCell(models.Model):
    deviceId = models.TextField()
    timestamp = models.BigIntegerField()
    lat = models.FloatField()
    lng = models.FloatField()
    packageId = models.IntegerField()
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()


class PathBlockManager(models.Manager):
    use_in_migrations = True

    def create(self, **validated_data):
        path_block = self.model(**validated_data)
        path_block.save(using=self._db)
        return path_block


class PathBlock(models.Model):
    objects = PathBlockManager()

    deviceId = models.TextField()
    timestampStart = models.BigIntegerField()
    timestampEnd = models.BigIntegerField()
    latStart = models.FloatField()
    lngStart = models.FloatField()
    latEnd = models.FloatField()
    lngEnd = models.FloatField()
    is_resolved = models.BooleanField(default=False)
    quakeDelta = models.OneToOneField('QuakeDelta', on_delete=models.CASCADE)


class QuakeDeltaManager(models.Manager):
    def create_delta_from_event_list(self, device_id, quake_event_list,):
        average_inclination = self._calculate_average_delta(quake_event_list)
        last_benchmark = PathBlock.objects.filter(Q(deviceId=device_id) & Q(Q(latStart=1000) & Q(lngStart=1000))).order_by('timestampEnd')[:1]
        if last_benchmark:
            delta = self.model(
                x=abs(last_benchmark.x - average_inclination['x']),
                y=abs(last_benchmark.y - average_inclination['y']),
                z=abs(last_benchmark.z - average_inclination['z']),
            )
            delta.save(using=self._db)

        else:
            delta = self.model(
                x=abs(average_inclination['x']),
                y=abs(average_inclination['y']),
                z=abs(average_inclination['z']),
            )
            delta.save(using=self._db)
        return delta

    def _calculate_average_delta(self, quake_event_list):
        x = 0
        y = 0
        z = 0
        for quake in quake_event_list:
            x += quake['x']
            z += quake['z']
            y += quake['y']
        return {'x': x/len(quake_event_list), 'y': y/len(quake_event_list), 'z': z/len(quake_event_list)}

class QuakeDelta(models.Model):
    objects = QuakeDeltaManager()
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()




