from django.db import models
from django.utils.timezone import datetime, timedelta
from inventory.local import DEFAULT_EXPIRATION

# Create your models here.

class Distributor(models.Model):
    distributor_name = models.CharField(max_length=200)

    url = models.URLField()

    supplier_notes = models.TextField(null=True)

    def __str__(self):
        return self.distributor_name

    def item_count(self):

        count = len(self.objects.all())

        return count


class Product(models.Model):
    barcode_id = models.BigIntegerField()
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    notes = models.TextField(null=True)

    #TODO: fix this
    product_number = models.BigIntegerField(default=0)

    now = datetime.now()
    date_first_added = models.DateTimeField('date added', default=now)

    def __str__(self):
        return self.name

    def __int__(self):
        return self.return_quantity()

    @property
    def quantity(self):

        item_set = self.item_set.all()
        quantity = len(item_set)

        return quantity

    # def update_quantity(self):
    #     self.quantity = len(self.item_set.all())
    #     return self.quantity

    @property
    def items_checked_out(self):

        item_set = self.item_set.all()

        quantity_checked_out = 0

        for item in item_set:

            if not item.checked_in:

                quantity_checked_out += 1

        return quantity_checked_out

    @property
    def average_cost(self):

        if self.quantity > 0:

            item_set = self.item_set.all()

            total_cost = 0

            for item in item_set:
                total_cost += item.cost

            quantity = self.quantity

            average_item_cost_raw = total_cost / quantity

        else:

            average_item_cost_raw = 0

        average_item_cost = '${:20,.2f}'.format(average_item_cost_raw)

        return average_item_cost
    #
    # @property
    # def formatted_average_cost(self):
    #
    #     cost = '${:20,.2f}'.format(self.average_cost)
    #
    #     return cost


class Item(models.Model):
    product = models.ForeignKey(Product)

    #TODO fix this
    distributor = models.ForeignKey(Distributor, null=True)

    #TODO fix this too
    item_number = models.BigIntegerField(default=0)
    checked_in = models.BooleanField(default=True)

    expiration_date = models.DateField()

    lot_number = models.BigIntegerField(null=True)

    cost = models.DecimalField(decimal_places=2, max_digits=8)

    location_room = models.CharField(max_length=200, null=True)
    location_unit = models.CharField(max_length=200, null=True)
    location_shelf = models.CharField(max_length=200, null=True)

    def __str__(self):

        something = '{product} with lot #{number}'.format(
            product=self.product.name,
            number=str(self.lot_number)
        )

        return something

    @property
    def formatted_cost(self):

        cost = '${:20,.2f}'.format(self.cost)

        return cost

    @property
    def location(self):

        location = 'Room: {room}, Unit: {unit}, Shelf: {shelf}'.format(
            room=self.location_room,
            unit=self.location_unit,
            shelf=self.location_shelf,
        )

        return location


class LocationRoom(models.Model):

    room_id = models.CharField(max_length=200)

    room_name = models.CharField(max_length=200)

    def __str__(self):

        return self.room_id

    @property
    def item_count(self):

        count = len(self.item_set.all())

        return count

    @property
    def items(self):

        items = self.item_set.all()

        return items

    @property
    def unit_count(self):

        count = len(self.unit_set.all())

        return count

    @property
    def units(self):

        units = self.unit_set.all()

        return units


class LocationUnit(models.Model):

    unit_id = models.CharField(max_length=200)

    room = models.ForeignKey(LocationRoom)

    unit_type = models.CharField(max_length=200)
    #TOOD remove temp, and merge into type
    unit_temperature = models.CharField(max_length=200, null=True)

    def __str__(self):

        return self.unit_id

    @property
    def item_count(self):

        count = len(self.item_set.all())

        return count

    @property
    def items(self):

        items = self.item_set.all()

        return items

    @property
    def shelf_count(self):

        count = len(self.locationshelf_set.all())

        return count

    @property
    def shelves(self):

        shelves = self.locationshelf_set.all()

        return shelves


class LocationShelf(models.Model):

    shelf_id = models.CharField(max_length=200)

    unit = models.ForeignKey(LocationUnit)

    def __str__(self):

        return self.shelf_id

    @property
    def item_count(self):

        count = len(self.item_set.all())

        return count

    @property
    def items(self):

        items = self.item_set.all()

        return items