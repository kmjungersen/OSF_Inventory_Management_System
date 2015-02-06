__author__ = 'kurtisjungersen'

DB_NODE = '192.168.33.11'

DB_PORT = 8888

# Products and items are listed as a tuple in the form of (<item>, <required>),
# to indicate whether the field MUST be updated after every edit

# TODO - add a third item to each tuple defining what type of field it is

PRODUCT_FIELDS = [
    ('product_number', False),
    ('name', False),
    ('quantity', True),
    ('items', True),
    ('description', False),
    ('notes', False),
    ('preferred_supplier', False),
    ('supplier_notes', False),
    ('container_type', False),
    ('average_cost', True),
]

ITEM_FIELDS = [
    ('barcode_id', True),
    ('item_number', True),
    ('expiration_date', True),
    ('room', True),
    ('unit', True),
    ('shelf', True),
    ('date_added', True),
    ('most_recently_used', True),
    ('purchased_from', True),
    ('cost', True),
    ('checked_in', True),
]

FIELDS = [
    'barcode_id',
    'name',
    'quantity',
    'expiration_date',
    'description',
    'notes',
    'quantity',
    'container_type',
    'room',
    'unit',
    'shelf',
    'container',
    'slot_number',
    'date_added',
    'most_recently_used',
    'purchased_from',
    'cost',
    'average_cost',
    'preferred_supplier',
    'supplier_notes',
]

REQUIRED_FIELDS = [
    'barcode_id',
    'name',
    'quantity',
    'expiration_date',
]

CONTAINER_TYPES = [
    'milk_jug',
    'egg_carton',
    'box_set',
    'individual_item',
]

# DATA_TYPES = {
#     'barcode_number': 'int',
#     'item_number': 'int',
#     'manufacturer_id': 'int',
#     'quantity': 'int',
#     'container_type': 'str',
#     'room': 'str',
#     'unit': 'int',
#     'shelf': 'int',
#     'container': 'int',
#     'slot_number': 'int',
#     'description': 'str',
#     'notes': 'str',
#     'date_added': 'date',
#     'expiration_date': 'date',
#     'most_recently_used': 'date',
#     'preferred_supplier': 'str',
#     'supplier_notes': 'str',
#     'average_cost': 'float',
# }