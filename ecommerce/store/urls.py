from django.urls import path
from . import views

urlpatterns = [
    path('', views.store, name='store'),
    
    #Indiviaual Product
    path('product/<slug:product_slug>/', views.product_info, name='product-info'),
    
    #Indiviaual Category
    path('search/<slug:category_slug>/', views.list_category, name='list-category'),
   
]
