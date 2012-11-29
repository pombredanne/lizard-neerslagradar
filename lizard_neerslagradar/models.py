#import datetime

from lizard_map import coordinates

from django.contrib.auth.models import User
from django.contrib.gis.db import models


class Region(models.Model):
    """Users are connected to one or more Regions. They are gemeentes,
    waterschappen etc."""

    name = models.CharField(max_length=200)
    geometry = models.PolygonField(srid=4326)  # WGS84
    objects = models.GeoManager()
    users = models.ManyToManyField(User)

    def __unicode__(self):
        return self.name

    def google_extent(self):
        xmin, ymin, xmax, ymax = self.geometry.extent
        xming, yming = coordinates.wgs84_to_google(xmin, ymin)
        xmaxg, ymaxg = coordinates.wgs84_to_google(xmax, ymax)
        return xming, yming, xmaxg, ymaxg

    @classmethod
    def extent_for_user(cls, user):
        if not user.is_authenticated():
            return None

        regions = user.region_set.all()
        if not regions:
            return None

        google_extents = [region.google_extent() for region in regions]

        extents = [{
                'left': xmin,
                'bottom': ymax,
                'right': xmax,
                'top': ymin
                } for xmin, ymin, xmax, ymax in google_extents]

        return {
            'left': str(min(extent['left'] for extent in extents)),
            'bottom': str(max(extent['bottom'] for extent in extents)),
            'right': str(max(extent['right'] for extent in extents)),
            'top': str(min(extent['top'] for extent in extents))
            }
