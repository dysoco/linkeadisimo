# Generated by Django 3.0.1 on 2019-12-27 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20191226_1237'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='publication',
            name='is_text',
        ),
    ]
