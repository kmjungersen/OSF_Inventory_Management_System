__author__ = 'kurtisjungersen'

DB_NODE = '192.168.33.11'

DB_PORT = 27017

# Products and items are listed as a tuple in the form of (<item>, <required>),
# to indicate whether the field MUST be updated after every edit

# TODO - add a third item to each tuple defining what type of field it is
# TODO - add a fourth item to each tuple defining required setup fields

# TODO - change 'product_number' to 'product_id' and same for items

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

# CONTAINER_TYPES = [
#     'milk_jug',
#     'egg_carton',
#     'box_set',
#     'individual_item',
# ]

CONTAINERS = {
    'milk_jug': [
        ('size', False),
        ('estimated_remaining', True),
    ],
    'egg_carton': [
        ('container_capacity', False),
        ('quantity_remaining', True),
    ],
    'box_set': [
        ('set_contents', False)
    ],
    'individual_item': [

    ],
}

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