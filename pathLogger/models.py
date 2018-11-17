from django.db import models

# Create your models here.
from django.db import models
from django.db.models import Q

class PathBlockManager(models.Manager):
    use_in_migrations = True

    def create(self, **validated_data):
        path_block = self.model(**validated_data)
        path_block.save(using=self._db)
        return path_block


class PathBlock(models.Model):
    objects = PathBlockManager()

    timestampStart = models.DateTimeField()
    timestampEnd = models.DateTimeField()
    latStart =models.FloatField()
    lngStart =models.FloatField()
    latEnd =models.FloatField()
    lngEnd =models.FloatField()

class QuakeEvent(models.Model):
    parent_path = models.ForeignKey('PathBlock', on_delete=models.CASCADE,)
    x = models.FloatField()
    y = models.FloatField()
    z = models.FloatField()

