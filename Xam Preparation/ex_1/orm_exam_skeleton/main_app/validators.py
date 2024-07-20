from django.core.exceptions import ValidationError


class RangeValidator:
    def __init__(self, min_value, max_value, message=None):
        self.min_value = min_value
        self.max_value = max_value
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value is None:
            self.__message = f"The rating must be between {self.min_value:.1f} and {self.max_value:.1f}"
        else:
            self.__message = value

    def deconstruct(self):
        return (
            'main_app.validators.RatingValidator',
            [self.min_value, self.max_value],
            {"message": self.message},
        )
