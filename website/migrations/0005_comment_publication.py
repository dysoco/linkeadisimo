# Generated by Django 3.0.2 on 2020-01-11 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_remove_comment_publication'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='publication',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='website.Publication'),
        ),
    ]
