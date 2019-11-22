from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)

    class Meta:
        ordering = ['title']

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title} - {self.slug}'

class Subcategory(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    category = models.ForeignKey(Category, related_name="subcategories", on_delete=models.CASCADE)

    class Meta:
        ordering = ['title']

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.category.title} - {self.title} - {self.slug}'

class Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    thumbnail = models.ImageField()
    subcategory = models.ForeignKey(Subcategory, related_name="products", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.subcategory.title} - {self.title} - {self.price}'

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return f'{self.product.title} - {self.image}'
