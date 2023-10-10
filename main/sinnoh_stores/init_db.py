from .models import *
from decimal import *

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
#     f.close()