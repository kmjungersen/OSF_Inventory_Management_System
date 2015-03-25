__author__ = 'kmjungersen'


from pyscan.main import Barcode
from functools import wraps
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


