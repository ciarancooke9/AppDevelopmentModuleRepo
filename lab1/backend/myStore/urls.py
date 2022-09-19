from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name="index"),
   path('products', views.all_products, name="products"),
   path('products/<int:product_id>', views.product_individual, name="individual_product" ),
]