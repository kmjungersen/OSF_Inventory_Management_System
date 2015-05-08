from inventory.models import Item, Product
import random


number = 10


for i in range(int(number)):

    p = Product()

    p.barcode_id = i * 100
    p.name = 'Product #{i}00'.format(i=i)
    p.description = 'foo'
    p.notes = 'foooooo'
    p.save()

    for j in range(int(number)):

        item = Item()

        item.product = p
        item.cost = random.randrange(2, 100)
        item.save()