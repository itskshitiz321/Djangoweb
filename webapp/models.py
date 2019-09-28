from django.db import models

# Create your models here.
class pointofinterests(models.Model):
    name = models.CharField(max_length=30)
    lat = models.FloatField()
    lon = models.FloatField()
    alt=models.FloatField()