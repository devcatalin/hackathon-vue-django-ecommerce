from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    USER_TYPE_CHOICES = (
        ('seller', 'Seller'),
        ('buyer', 'Buyer'),
        ('manager', 'Manager')
    )

    BUYER_TYPE_CHOICES = (
        ('private', 'Private'),
        ('company', 'Company')
    )

    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)
    buyer_type = models.CharField(max_length=10, choices=BUYER_TYPE_CHOICES)

    # @property
    # def is_seller(self):
    #     return user_type == 'seller'

    # @property
    # def is_buyer(self):
    #     return user_type == 'buyer'
