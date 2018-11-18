from django.db import models
from pathLogger.models import PathBlock
from math import cos


class ResolvedPathManager(models.Manager):
    def resolve_path(self, all_paths_on_place):
        for path in all_paths_on_place:
            pass
    def impose(self):
        unresolved_paths = PathBlock.objects.filter(is_resolved=False)
        path_stacks = ResolvedPath.objects.all()
        for new_path in unresolved_paths:

            exists = False
            for path_stack in path_stacks:
                if path_stack.does_belong(new_path):
                    exists = True
                    path_stack.add_to_stack(new_path.quakeDelta)
            if not exists:
                new_stack = ResolvedPath.objects.create(
                    latStart = new_path.latStart,
                    lngStart = new_path.lngStart,
                    latEnd = new_path.latEnd,
                    lngEnd = new_path.lngEnd,
                )
                path_stacks.union(new_stack)

        unresolved_paths.update(is_resolved=True)
        return path_stacks



class ResolvedPath(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    latStart = models.FloatField()
    lngStart = models.FloatField()
    latEnd = models.FloatField()
    lngEnd = models.FloatField()
    color = models.TextField()
    objects = ResolvedPathManager()

    def does_belong(self, other_path):
        other_path_lat_start = other_path.latStart
        other_path_lng_start = other_path.lngStart
        return abs(self.latStart - other_path_lat_start) < self.max_latitude_delta and \
                 abs(self.lngStart - other_path_lng_start) < self.max_longitude_delta

    def add_to_stack(self, delta):
        ResolvedDelta.objects.create(
            path = self,
            x=delta.x,
            y=delta.y,
            z=delta.z

            )

    def average_delta(self):
        x = 0
        y = 0
        z = 0
        deltas = ResolvedDelta.objects.filter(path=self)
        for delta in deltas:
            x +=delta.x
            y +=delta.y
            z +=delta.z
        return {'x':x/len(deltas), 'y':y/len(deltas), 'z':z/len(deltas)}

    @property
    def max_longitude_delta(self):
        one_degree= 111132.954 * cos(self.latStart)
        return 10/one_degree

    @property
    def max_latitude_delta(self):
        return 0.0000898230

class ResolvedDelta(models.Model):
    path = models.ForeignKey(ResolvedPath, on_delete=models.CASCADE)
    x= models.FloatField()
    y= models.FloatField()
    z= models.FloatField()
