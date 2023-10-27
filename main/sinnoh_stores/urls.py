from . import views
from django.urls import path

urlpatterns = [
    path('get-locations', views.shop_locations),
    path('get-products', views.products_and_locations),
    path('get-stock', views.check_stock),
    path('reset-stock', views.reset_stock),
]