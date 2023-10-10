from django.shortcuts import render
from django.http import JsonResponse
from .models import ShopLocation

# Create your views here.
def shop_locations(request):
    """
    Returns location info about each shop in sinnoh as JSON.
    """
    shops = ShopLocation.objects.all()
    shop_data = []
    for shop in shops:
        dict_so_far = {}
        dict_so_far['name'] = shop.name
        dict_so_far['lat'] = shop.lat
        dict_so_far['lng'] = shop.lng
        shop_data.append(dict_so_far)

    return JsonResponse(shop_data, safe=False)