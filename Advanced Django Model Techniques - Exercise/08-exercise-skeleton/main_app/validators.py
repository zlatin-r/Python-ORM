from django.core.exceptions import ValidationError


def validate_name(value):
    if not value.isalpha() and not value.isspace():
        raise ValidationError("Name can only contain letters and spaces")
