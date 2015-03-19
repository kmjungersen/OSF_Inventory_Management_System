#! /usr/bin/env python

import os
import sys


try:
    app = sys.argv[1]

except ValueError:
    exit('Error!  Please use the app name to complete migrations.')

dir = '{app}/migrations'.format(
    app=app,
)

base_command = 'python manage.py '

migration_list = os.listdir(dir)

migration_number = 1

for file_name in migration_list:

    mig_number = file_name.split('_')[0]

    try:
        number = int(mig_number)

    except (ValueError):
        pass

    if number >= migration_number:
        migration_number = number

migration_number += 1

migration = '{:04}'.format(
    migration_number
)

commands = [
    'makemigrations {app}',
    'sqlmigrate {migration}',
    'migrate'
]

for cmd in commands:

    command = base_command + cmd.format(
        migration=migration,
        app=app,
    )
    os.system(command)