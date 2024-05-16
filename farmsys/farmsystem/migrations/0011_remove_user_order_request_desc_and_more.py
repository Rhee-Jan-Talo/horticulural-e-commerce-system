# Generated by Django 4.0.5 on 2022-08-12 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmsystem', '0010_user_order_request'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_order_request',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='user_order_request',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='user_order_request',
            name='units',
        ),
        migrations.AddField(
            model_name='user_order_request',
            name='quantity_variations_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
