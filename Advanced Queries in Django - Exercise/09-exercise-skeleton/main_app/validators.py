from django.core.exceptions import ValidationError


def rating_validator(value):
    if 0 > value > 10:
        raise ValidationError("The rating must be between 0.0 and 10.0")
