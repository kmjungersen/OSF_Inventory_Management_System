from django.db import models
from django.utils.timezone import datetime, timedelta
from inventory.local import DEFAULT_EXPIRATION

# Create your models here.


class Product(models.Model):
    barcode_id = models.BigIntegerField()
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    notes = models.TextField(null=True)

    #TODO: fix this
    product_number = models.BigIntegerField(default=0)

    now = datetime.now()

    date_first_added = models.DateTimeField('date added', default=now)
    foo = 5

    def __str__(self):
        return self.name

    def __int__(self):
        return len(self.item_set.all())

    def __return_quantity(self):
        return int(self)

    def _compute_average_price(self):
        pass


class Item(models.Model):
    product = models.ForeignKey(Product)

    item_number = models.BigIntegerField(default=0)

    default_expiration = timedelta(days=DEFAULT_EXPIRATION) + datetime.now()
    expiration_date = models.DateField(default=default_expiration)

    lot_number = models.BigIntegerField(null=True)

    cost = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self):

        something = 'item #{number} of {product}'.format(
            product=self.product.name,
            number=str(self.lot_number)
        )

        return something