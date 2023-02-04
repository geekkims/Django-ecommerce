from django.contrib import admin

from store.models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=('product_name','slug','category','price','stock','is_available','modified_field')
    prepopulated_fields = {'slug': ('product_name',)}



admin.site.register(Product,ProductAdmin)
