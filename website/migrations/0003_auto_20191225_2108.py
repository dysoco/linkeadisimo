# Generated by Django 3.0.1 on 2019-12-26 00:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('website', '0002_auto_20191224_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='publication',
            name='title',
            field=models.CharField(default='NONE', max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='publication',
            name='link',
            field=models.URLField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='publication',
            name='text',
            field=models.TextField(blank=True, default=''),
        ),
    ]
