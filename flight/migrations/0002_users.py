# Generated by Django 4.1.3 on 2022-11-25 17:53

from django.conf import settings
from django.db import migrations
from django.contrib.auth.management import create_permissions
from django.db import transaction

def create_users(apps, editor):

    for app_config in apps.get_app_configs():
        app_config.models_module = True
        create_permissions(app_config, verbosity=0)
        app_config.models_module = None
    User = apps.get_model(settings.AUTH_USER_MODEL)
    User.objects.create_superuser('admin', 'admin@mail.com', '1234')
    User.objects.create_user('manager', 'manager@mail.com', '1234')
    User.objects.create_user('operation', 'manager@mail.com', '1234')
    User.objects.create_user('pilot', 'pilot@mail.com', '1234')
    # breakpoint()
    
    u = User.objects.create_user('meu_pilot', 'pilot@mail.com', '1234')

    with transaction.atomic():
        Permission = apps.get_model("auth.Permission")
        permission = Permission.objects.get(codename='view_flightinstance')
        u.user_permissions.add(permission)

class Migration(migrations.Migration):

    dependencies = [
        ('flight', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_users, migrations.RunPython.noop),
    ]
