from decimal import Decimal

from django.db import models
from django.db.models import Q

from main_app.models import RealEstateListing


class RealEstateListingManager(models.Manager):

    def by_property_type(self, property_type: str):
        return RealEstateListing.objects.filter(property_type=property_type)

    def in_price_range(self, min_price: Decimal, max_price: Decimal):
        query = Q(price__gt=min_price, price__lte=max_price)
        return RealEstateListing.objects.filter(query)

    def with_bedrooms(self, bedrooms_count: int):
        return RealEstateListing.objects.filter(bedrooms_count=bedrooms_count)

    def popular_locations(self):
        pass
