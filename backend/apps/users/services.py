from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError

from .models import UserProfile


def create_user(
    *,
    username,
    email,
    password,
    user_type,
    full_name,
    phone_number,
    address,
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
            user_type=user_type,
            full_name=full_name,
            phone_number=phone_number,
            address=address,
            buyer_type=buyer_type
        )
    except Exception as e:
        raise ValidationError(e)

    user.profile = profile
    user.save()

    return User.objects.get(username=username)


def update_user(
    *,
    user,
    full_name,
    phone_number,
    address
):
    pass
