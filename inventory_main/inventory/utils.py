__author__ = 'kmjungersen'


from pyscan.main import Barcode
from functools import wraps
from inventory.models import Product, Item
import errno
import os
import signal


class TimeoutError(Exception):
    pass


def timeout(seconds=10, error_message=os.strerror(errno.ETIME)):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wraps(func)(wrapper)

    return decorator

# @timeout(3)
def query_upc_database(barcode_id):
    """

    :param barcode_id:
    :return:
    """

    b = Barcode(barcode_id)

    data = b.data

    result = None

    if len(data) == 1:

        info = data.get('0')

        if info.get('productname') == ' ':

            pass

        else:

            result = [info]

    elif len(data) == 0:

        pass

    else:

        info = []

        for key, value in data.items():

            info.append(value)

        result = info

    return result


def lookup_item(barcode_id, item_id):

    product = Product.objects.get(barcode_id__exact=barcode_id)

    item = product.item_set.get(id__exact=item_id)

    return item

def lookup_product(barcode_id, new_product=False):

    product_found = False
    product_name = ''
    description = ''
    # error_message = ''

    try:
        product = Product.objects.get(barcode_id__exact=barcode_id)

        product_found = True
        product_name = product.name
        description = product.description

        return product

    except Exception:

        if new_product:

            data = query_upc_database(barcode_id)

            print(data)

            if data:

                product_name = data[0].get('productname')

                return product_name

    return None