from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import pointofinterests

# Register your models here.
class agricultureadmin(LeafletGeoAdmin):
    list_display=('name','alt')
    settings_overrides =  {
        'DEFAULT_CENTER': (28.3949, 84.1240),
        'DEFAULT_ZOOM': 7,
        'MIN_ZOOM': 3,
        'MAX_ZOOM': 18,
        'TILES': [('Google Terrain','http://mt0.google.com/vt/lyrs=p&hl=en&x={x}&y={y}&z={z}',''),('OSM','//{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',''),('Google Satellite','http://mt0.google.com/vt/lyrs=s&hl=en&x={x}&y={y}&z={z}','')],
    }
admin.site.register(pointofinterests,agricultureadmin)