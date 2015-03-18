from django.db import models

# Create your models here.


class Product(models.Model):
    barcode_id = models.BigIntegerField()
    name = models.CharField(max_length=200)
    product_number = models.BigIntegerField()

    date_first_added = models.DateTimeField('date added')
    foo = 5


    def __str__(self):
        return self.name

    def __int__(self):
        return len(self.item_set.all())

    def __return_quantity(self):
        return int(self)


class Item(models.Model):
    product = models.ForeignKey(Product)

    item_number = models.BigIntegerField()

    expiration_date = models.DateTimeField()
    cost = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self):

        something = 'item #{number} of {product}'.format(
            product=self.product.name,
            number=str(self.item_number)
        )

        return something