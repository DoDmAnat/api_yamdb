from datetime import datetime

from django.core.exceptions import ValidationError


def validate_date(value):
    if value > datetime.now().year:
        raise ValidationError(
            ('Год создания произведения не может быть больше текущего!'),
            params={'value': value}, )
