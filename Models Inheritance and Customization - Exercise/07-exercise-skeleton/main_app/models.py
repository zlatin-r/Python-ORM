from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.

class BaseCharacter(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        abstract = True


class Mage(BaseCharacter):
    elemental_power = models.CharField(max_length=100)
    spellbook_type = models.CharField(max_length=100)


class Assassin(BaseCharacter):
    weapon_type = models.CharField(max_length=100)
    assassination_technique = models.CharField(max_length=100)


class DemonHunter(BaseCharacter):
    weapon_type = models.CharField(max_length=100)
    demon_slaying_ability = models.CharField(max_length=100)


class TimeMage(Mage):
    time_magic_mastery = models.CharField(max_length=100)
    temporal_shift_ability = models.CharField(max_length=100)


class Necromancer(Mage):
    raise_dead_ability = models.CharField(max_length=100)


class ViperAssassin(Assassin):
    venomous_strikes_mastery = models.CharField(max_length=100)
    venomous_bite_ability = models.CharField(max_length=100)


class ShadowbladeAssassin(Assassin):
    shadowstep_ability = models.CharField(max_length=100)


class VengeanceDemonHunter(DemonHunter):
    vengeance_mastery = models.CharField(max_length=100)
    retribution_ability = models.CharField(max_length=100)


class FelbladeDemonHunter(DemonHunter):
    felblade_ability = models.CharField(max_length=100)


class UserProfile(models.Model):
    username = models.CharField(max_length=70, unique=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True, blank=True)


class Message(models.Model):
    sender = models.ForeignKey(
        to=UserProfile,
        on_delete=models.CASCADE,
        related_name='sent_messages'
    )
    receiver = models.ForeignKey(
        to=UserProfile,
        on_delete=models.CASCADE,
        related_name='received_messages'
    )
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def mark_as_read(self):
        self.is_read = True
        self.save()

    def reply_to_message(self, reply_content):
        reply_message = Message.objects.create(
            sender=self.receiver,
            receiver=self.sender,
            content=reply_content
        )
        return reply_message

    def forward_message(self, receiver):
        forwarded_message = Message.objects.create(
            sender=self.receiver,
            receiver=receiver,
            content=self.content
        )
        return forwarded_message


class StudentIDField(models.PositiveIntegerField):

    def __init__(self, *args, **kwargs):
        kwargs['validators'] = [self.validate_student_id]
        super().__init__(*args, **kwargs)

    def to_python(self, value):
        if isinstance(value, int):
            return value
        try:
            value = int(value)
        except ValueError:
            raise ValueError("Invalid input for student ID")
        return value

    def validate_student_id(self, value):
        if value <= 0:
            raise ValidationError("ID cannot be less than or equal to zero")

    def get_prep_value(self, value):
        value = self.to_python(value)
        self.validate_student_id(value)
        return super().get_prep_value(value)


class Student(models.Model):
    name = models.CharField(max_length=100)
    student_id = StudentIDField()


class MaskedCreditCardField(models.CharField(max_length=20)):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

    def to_python(self, value):
        if isinstance(value, str):
            return value
        try:
            value = int(value)
        except ValueError:
            raise ValueError("The card number must be a string")
        return value


class CreditCard(models.Model):
    card_owner = models.CharField(max_length=100)
    card_number = MaskedCreditCardField(max_length=20)
