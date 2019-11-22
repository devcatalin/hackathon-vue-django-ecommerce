from rest_framework.exceptions import ValidationError

from .models import Product


def create_product(
    *,
    owner,
    title,
    price,
    description,
    thumbnail,
    subcategory
):
    if Product.objects.filter(owner=owner, title=title).exists():
        raise ValidationError("You already have a Product with the same title.")

    product = Product.objects.create(
        owner=owner,
        title=title,
        price=price,
        description=description,
        thumbnail=thumbnail,
        subcategory=subcategory
    )

    return Product.objects.get(pk=product.pk)
