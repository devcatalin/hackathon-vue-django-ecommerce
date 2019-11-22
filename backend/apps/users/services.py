from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError


def create_user(username, email, password):
    try:
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
            )
    except Exception as e:
        print(e)
        raise ValidationError("User could not be created.")
    return user
