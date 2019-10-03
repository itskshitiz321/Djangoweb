from django.contrib import admin
from .models import school
from leaflet.admin import LeafletGeoAdmin

# Register your models here.
class schooladmin(LeafletGeoAdmin):
    list_display=('name','Type')
    settings_overrides =  {
        'DEFAULT_CENTER': (28.333, 84.000),
        'DEFAULT_ZOOM': 7,
        'MIN_ZOOM': 5,
        'MAX_ZOOM': 24,
        'TILES': [('Google Terrain','http://mt0.google.com/vt/lyrs=p&hl=en&x={x}&y={y}&z={z}',''),('OSM','//{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',''),('Google Satellite','http://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}','')],
    }


admin.site.register(school,schooladmin)