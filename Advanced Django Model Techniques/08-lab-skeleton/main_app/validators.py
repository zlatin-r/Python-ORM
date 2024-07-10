from django.core.exceptions import ValidationError


def validate_menu_categories(value):
    required_categories = ["Appetizers", "Main Course", "Desserts"]

    for cat in required_categories:
        if cat.lower() not in value.lower():
            raise ValidationError(
                '"The menu must include each of the categories "Appetizers", "Main Course", "Desserts"."')
