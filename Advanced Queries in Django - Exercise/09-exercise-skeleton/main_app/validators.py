from django.core.exceptions import ValidationError


def rating_validator(value):
    if not 0 <= value <= 10:
        raise ValidationError("The rating must be between 0.0 and 10.0")


def release_year_validator(value):
    if not 1990 <= value <= 2023:
        raise ValidationError("The release year must be between 1990 and 2023")


# class RatingValidator:
#     def __init__(self, min_value, max_value, message):
#         self.min_value = min_value
#         self.max_value = max_value
#         self.message = message
#
#     @property
#     def message(self):
#         return self.__message
#
#     @message.setter
#     def message(self, value):
#         if value is None:
#             self.__message = f"The rating must be between {self.min_value:.1f} and {self.max_value:.1f}"
#         else:
#             self.__message = value
#
#     def __call__(self, value):
#         if not self.min_value <= value <= self.max_value:
#             raise ValidationError(self.message)
#
#     def deconstruct(self):
#         return (
#             'main_app.validators.RatingValidator',
#             [self.min_value, self.max_value],
#             {"message": self.message},
#         )
