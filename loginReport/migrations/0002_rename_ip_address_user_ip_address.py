# Generated by Django 3.2.4 on 2021-06-26 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginReport', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='IP_address',
            new_name='ip_address',
        ),
    ]