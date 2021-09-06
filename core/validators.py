import re

from django.core.exceptions import ValidationError


def phone_validator(phone: str):
    pattern = re.compile('^(9)(((1)|(3))([0-9])|(20)|(21))(\d{7})$')
    if not pattern.search(phone):
        raise ValidationError("Wrong Phone number")


def email_validator(email: str):
    ...
