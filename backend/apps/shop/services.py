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
    if Product.objects.filter(owner=owner).filter(title=title).exists():
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


def update_product(
    *,
    product_slug,
    owner=None,
    title=None,
    price=None,
    description=None,
    thumbnail=None,
    subcategory=None
):
    try:
        product = Product.objects.get(owner=owner, slug=product_slug)
    except Product.DoesNotExist:
        raise ValidationError("Could not find the specified Product.")

    if title:
        if Product.objects.filter(owner=owner).filter(title=title).exists():
            raise ValidationError("You already have a Product with the same title.")
        product.title = title

    if price:
        product.price = price

    if description:
        product.description = description

    if thumbnail:
        product.thumbnail = thumbnail

    if subcategory:
        product.subcategory = subcategory

    product.save()

    return Product.objects.get(pk=product.id)
