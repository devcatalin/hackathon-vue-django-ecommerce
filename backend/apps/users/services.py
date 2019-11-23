from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

from .models import UserProfile


def create_user(
    *,
    username,
    user_type,
    email,
    full_name,
    phone_number,
    address,
    latitude,
    longitude,
    password,
    buyer_type
):
    try:
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
    except Exception as e:
        raise ValidationError(e)

    try:
        profile = UserProfile.objects.create(
            user = user,
            user_type=user_type,
            full_name=full_name,
            phone_number=phone_number,
            address=address,
            latitude=latitude,
            longitude=longitude,
            buyer_type=buyer_type
        )
    except Exception as e:
        raise ValidationError(e)

    return User.objects.get(username=username)


def update_user(
    *,
    user,
    full_name,
    phone_number,
    address
):
    pass
