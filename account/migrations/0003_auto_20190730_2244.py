# Generated by Django 2.2.3 on 2019-07-30 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20190730_0657'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='region',
            new_name='target',
        ),
    ]