from django.urls import path
from . import views

app_name ="frontend"

urlpatterns = [
  
    path('',views.index,name="home"),
    # path('store/<slug:category_slug>/',views.store, name="products_by_category"),
    # path('category/<slug:category_slug>/<slug:product_slug>/',views.product_detail,name="product_detail"),
   

]