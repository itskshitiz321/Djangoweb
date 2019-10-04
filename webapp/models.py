from django.db import models
from django.contrib.gis.db import models as geomodels

# Create your models here.

class school(models.Model):
    SCHOOL_CHOICES =(
        ('Government','Government'),
        ('Private','Private'),
    )
    name = models.CharField(max_length=40)
    location = geomodels.PointField(srid=4326)
    Type = models.CharField(max_length=40, blank=True, choices=SCHOOL_CHOICES)
    
# class Profile(models.Model):
#     # ...

#     skills = models.ManyToManyField(
#         to='webapp.Skill',  # use a string in the format `app_name.model_name` to reference models to avoid issues using the model before it was defined
#         related_name='user_profiles',  # the name for that relation from the point of view of a skill
#     )

# class Skill(models.Model):
#     name = models.CharField(max_length=255)
#     abbreviation = models.CharField(max_length=3)
