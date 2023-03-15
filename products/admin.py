from django.contrib import admin
from . import models


# Register your models here.

class ProductImageInline(admin.TabularInline):
    model = models.ProductImage
    extra = 1


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_top', 'is_active')  # displaying on a page like a mini table
    list_filter = ('is_top', 'is_active')
    list_editable = ('is_top', 'is_active') # opportunity to change without entering inside
    search_fields = ('title', 'body')
    inlines = (ProductImageInline,)


admin.site.register(models.ProductImage)
admin.site.register(models.Product, ProductAdmin)
