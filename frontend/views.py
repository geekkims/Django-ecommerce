from django.shortcuts import get_object_or_404, render
from category.models import Category
from store.models import Product

# Create your views here.

def index(request):

    products_obj=Product.objects.all().filter(is_available=True)
    context={

        "products_obj":products_obj,

    }
    return render(request,'frontend/index.html',context)


