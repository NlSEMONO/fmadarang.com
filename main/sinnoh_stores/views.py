from django.shortcuts import render
from django.http import JsonResponse
from .models import *

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

def products_and_locations(request):
    """
    Returns all products information and locations they can be found in at stores in Sinnoh as JSON.
    """
    products = []
    product_listings = ProductLister.objects.all()
    shops = ShopLocation.objects.all()
    for prod in product_listings:
        locations = []
        for shop in shops: 
            if (len(shop.products.filter(name=prod.name)) > 0):
                locations.append(shop.name)
        print(prod)
        products.append({
            'id': prod.id,
            'name': prod.name,
            'price': prod.price,
            'locations': locations,
            'image': f'/Dream_{"_".join(prod.name.split(" "))}_Sprite.png'
        })
    
    return JsonResponse(products, safe=False)