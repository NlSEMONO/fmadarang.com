"""
FILE FOR INITILIAZING DATABASES BETWEEN DEVELOPMENT AND PRODUCTION
"""

from .models import *
from decimal import *

ITEMS_FILE = 'items_info'
STORES_FILE = 'store_info.txt'
ELEMENT_DELIMITER = ';'
ELEMENT_DELIMITER2 = ','

# def init_db():
#     all_inventories = Inventory.objects.all()

#     for inv in all_inventories:
#         if inv.name != 'Sandgem':
#             DEFAULT_INVENTORY = ShopLocation.objects.filter(name="Sandgem")[0].products.all()
#             print(DEFAULT_INVENTORY)

#             print(inv.name)
#             lat = input("\nLat:\n")
#             lng = input("Long:\n")
#             sl = ShopLocation(name=inv.name, lat=Decimal(lat), 
#                               lng=Decimal(lng),
#                               inventory=inv)
#             sl.save()
#             for item in DEFAULT_INVENTORY:
#                 sl.products.add(item)
#             sl.save()
# def print_store_locs_to_file():
#     f = open('store_info.txt', 'w')
#     all_info = ShopLocation.objects.all()
#     for shop in all_info:
#         str_to_write = f'{shop.name};{shop.lat};{shop.lng};'
#         for item in shop.products.all():
#             str_to_write += f'{item.name},'
#         f.write(str_to_write+"\n")
# #     f.close()


# def print_items_to_file():
#     f = open('items_info', 'w')
#     all_items = ProductLister.objects.all()
#     for item in all_items:
#         f.write(f'{item.name};{item.price}\n')
def write_inventories():
    f = open('inventories', 'w')
    all_inventories = Inventory.objects.all()
    for inv in all_inventories:
        f.write(f'{inv.name}\n')

def load_items_from_file():
    with open('items_info') as f:
        for line in f:
            data = line.split(ELEMENT_DELIMITER)
            data[1] = int(data[1][:-1])
            print(data)
def load_inventories():
    with open('inventories', 'r') as f:
        for line in f:
            print(line[:-1])

def add_items_with_defaults_to_stores():
    all_stores = ShopLocation.objects.all()
    for shop in all_stores:
        inv = shop.inventory
        for item in shop.products.all():
            new_prod = ProductTracker(name=item.name, quantity=30, inventory=inv)
            new_prod.save()