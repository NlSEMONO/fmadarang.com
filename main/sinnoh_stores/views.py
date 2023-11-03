from django.shortcuts import render
from django.http import JsonResponse
from .models import *
import json
import hashlib
import random

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

def check_stock(request):
    """"
    Returns the stock of an item in a given store as JSON.
    """
    try:
        data = request.body.decode('utf-8')
        data = request.GET

        shop = ShopLocation.objects.filter(name=data['shop'])[0]
        inv = shop.inventory
        item = ProductTracker.objects.filter(name=data['item'], inventory=inv)[0]
        return JsonResponse({'quantity': item.quantity})
    except:
        return JsonResponse({'quantity': -1})


def reset_stock(request):
    """
    Resets all shop's stock of every item to 30.
    """
    shops = ShopLocation.objects.all()
    for shop in shops:
        inv = shop.inventory
        available_prods = ProductTracker.objects.fitler(inventory=inv)
        for item in available_prods:
            item.quantity = 30
            item.save()
    
    return JsonResponse({'success': True})


def generate_id():
    all_chars = list('abcdefghijklmnopqrstuvwxyz')
    all_chars.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    all_chars.extend(list('1234567890'))
    while True:
        str_so_far = ''
        for _ in range(0, 9):
            str_so_far += random.choice(all_chars)
        key = hashlib.sha256(str_so_far.encode('utf-8')).hexdigest()
        if len(ShoppingCart.objects.filter(hashed_id=key) == 0):
            return key
    

def new_session(request):
    """
    Creates a new shopping cart session and returns the id of the cart as JSON.
    """
    cart = ShoppingCart(hashed_id=generate_id())
    cart.save()
    return JsonResponse({'session': cart.hashed_id})


def get_session_data(request):
    """
    Returns a Shopping Cart's information given a session id as JSON
    """
    data = request.body.decode('utf-8')
    data = json.loads(data)
    cart = ShoppingCart.objects.filter(hashed_id=data['session'])[0]
    inv = cart.products
    
    items = ProductTracker.objects.filter(inventory=inv)
    items_so_far = []
    for item in items:
        items_so_far.append({
            'name': item.name,
            'quantity': item.quantity,
        })
    return JsonResponse({'data': items_so_far})