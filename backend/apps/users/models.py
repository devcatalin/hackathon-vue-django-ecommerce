from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    USER_TYPE_CHOICES = (
        ('seller', 'Seller'),
        ('buyer', 'Buyer')
    )

    BUYER_TYPE_CHOICES = (
        ('private', 'Private'),
        ('company', 'Company')
    )

    user = models.OneToOneField(User, related_name="buyer", on_delete=models.CASCADE)
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=255)
    buyer_type = models.CharField(max_length=10, choices=BUYER_TYPE_CHOICES)

    @property
    def is_seller(self):
        return user_type == 'seller'

    @property
    def is_buyer(self):
        return user_type == 'buyer'
