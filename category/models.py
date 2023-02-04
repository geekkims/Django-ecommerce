from django.db import models
import uuid

from django.urls import reverse

# Create your models here.

def cat_image_upload_to(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4().hex}.{ext}"
    return f"cat_image/{filename}"

class Category(models.Model):
    category_name=models.CharField(max_length=255)
    slug=models.SlugField(max_length=255,unique=True)
    description=models.TextField(max_length=255,blank=True)
    cat_image=models.ImageField(upload_to=cat_image_upload_to,blank=True)

    class  Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
 
    def get_url(self):
            return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        return str(self.category_name)