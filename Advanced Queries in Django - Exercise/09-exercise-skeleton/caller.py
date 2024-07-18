import os

import django
from django.db import models


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

from main_app.models import RealEstateListing


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

# Run the 'by_property_type' method
house_listings = RealEstateListing.objects.by_property_type('House')
print("House listings:")
for listing in house_listings:
    print(f"- {listing.property_type} in {listing.location}")