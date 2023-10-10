from django.db import models


class ProductLister(models.Model):
    """
    Stores a product as a standalone item with a price. Used to store information about products, 
    which are not tied to an individual store.

    Attributes: 
    - name: name of product
    - price: cost of product in PokeDollars
    """
    name = models.CharField(default="", max_length=128)
    price = models.PositiveIntegerField(default=1000)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    """
    Tracks number of products in a given inventory (works for orders and store inventories)

    name: what object's inventory this is
    """
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
    

class ProductTracker(models.Model):
    """
    Stores a product as an item in an inventory. Used to store information about a product's quantity
    in a store.

    Attributes: 
    - name: name of product
    - quantity: quantity of product
    - inventory: the inventory that the product is tied to
    """
    name = models.CharField(default="", max_length=128)
    quantity = models.PositiveIntegerField(default=100)
    inventory = models.ForeignKey(
        Inventory,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class ShopLocation(models.Model):
    """
    A physical store in the Sinnoh region with stuff to buy

    Attributes: 
    - name: city the store is in
    - lat: latitude of the irl equivalent of the pokemon city this shop is in
    - long: longitude of the irl equivalent of the pokemon city this shop is in
    - products: list of product offered in store
    """
    name = models.CharField(default="", max_length=128)
    lat = models.DecimalField(default=0, decimal_places=4, max_digits=7)
    lng = models.DecimalField(default=0, decimal_places=4, max_digits=7)
    products = models.ManyToManyField(
        ProductLister
    )
    inventory = models.OneToOneField(
        Inventory,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Order(models.Model): 
    """
    Stores information about an online order.
    """
    hashed_id = models.CharField(primary_key=True, max_length=64)
    orderer = models.CharField(default="", max_length=128)
    products = models.OneToOneField(
        Inventory,
        on_delete=models.CASCADE
    )
    pickup = models.ForeignKey(
        ShopLocation, 
        on_delete=models.RESTRICT
    )

    def __str__(self):
        return f'{self.orderer}: {self.hashed_id}'