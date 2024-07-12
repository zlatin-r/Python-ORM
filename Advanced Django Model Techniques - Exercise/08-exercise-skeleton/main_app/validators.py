from django.core.exceptions import ValidationError


def letters_and_space_validator(value):
    if not value.isalpha() and not value.isspace():
        raise ValidationError("Name can only contain letters and spaces")
