import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _  # Needed for translation and localisation


# SUPER ADMIN
# MANAGER
# SHOP
# CUSTOMER

# Create your models here.
class Product(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=100, verbose_name=_('Title'), unique=True)
    body = models.TextField(verbose_name=_('Body'))
    main_image = models.ImageField(upload_to='products/%Y/%m/%d/', verbose_name=_('Main Image'))
    is_top = models.BooleanField(default=False, verbose_name=_('Is Top?'))
    is_active = models.BooleanField(default=True, verbose_name=_('Is Active?'))
    data = models.JSONField(default=dict, verbose_name=_('Data'))  # if we want to store as a dict especially not initialized

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('is_top', '-created_at',)
        verbose_name = _('Product')
        verbose_name_plural = _('Products')


class ProductImage(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    product = models.ForeignKey(
        to=Product,
        on_delete=models.CASCADE,
        related_name='product_images',
        verbose_name=_('Product')
    )
    image = models.ImageField(upload_to='product-images/%Y/%m/%d/', verbose_name=_('Image'))

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = _('Product Image')
        verbose_name_plural = _('Product Images')
