import os
from decimal import Decimal

import django
from django.db import models
from django.db.models import F, Q

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

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


# Create instances of RealEstateListing with locations
RealEstateListing.objects.create(
    property_type='House',
    price=100000.00,
    bedrooms=3,
    location='Los Angeles')
RealEstateListing.objects.create(
    property_type='Flat',
    price=75000.00,
    bedrooms=2,
    location='New York City')
RealEstateListing.objects.create(
    property_type='Villa',
    price=250000.00,
    bedrooms=4,
    location='Los Angeles')  # Same location as the first instance
RealEstateListing.objects.create(
    property_type='House',
    price=120000.00,
    bedrooms=3,
    location='San Francisco')