from django.db import models
import uuid

from django.urls import reverse

from category.models import Category

# Create your models here.

def pro_image_upload_to(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4().hex}.{ext}"
    return f"product_images/{filename}"



class Product(models.Model):
    product_name=models.CharField(max_length=255)
    slug=models.SlugField(max_length=255,unique=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    description=models.TextField(max_length=255,blank=True)
    price=models.IntegerField()
    images=models.ImageField(upload_to=pro_image_upload_to)
    stock=models.IntegerField()
    is_available=models.BooleanField(default=True)
    created_date=models.DateTimeField(auto_now_add=True)
    modified_field=models.DateTimeField(auto_now=True)


    def get_url(self):
        return reverse('products_detail',args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name
    

