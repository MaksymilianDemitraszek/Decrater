from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.ResolvedPath)
admin.site.register(models.ResolvedDelta)


