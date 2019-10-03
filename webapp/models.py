from django.db import models
from django.contrib.gis.db import models as geomodels

# Create your models here.

class school(models.Model):
    name = models.CharField(max_length=40)
    location = geomodels.PointField(srid=4326)
    Type = models.CharField(max_length=40, blank=True)