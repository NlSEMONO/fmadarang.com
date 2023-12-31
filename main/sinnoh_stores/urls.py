from . import views
from django.urls import path

urlpatterns = [
    path('get-locations', views.shop_locations),
    path('get-products', views.products_and_locations),
    path('get-product', views.get_product),
    path('get-stock', views.check_stock),
    path('reset-stock', views.reset_stock),
    path('new-session', views.new_session),
    path('get-session-data', views.get_session_data),
    path('add-to-cart', views.add_to_cart),
    path('checkout', views.checkout)
]