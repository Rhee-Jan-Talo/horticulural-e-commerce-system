# Generated by Django 4.1 on 2022-09-02 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farmsystem', '0029_delivery_info_payment_methods_refund_details'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='refund_details',
            new_name='refund_info',
        ),
        migrations.AlterField(
            model_name='delivery_info',
            name='date_arrived',
            field=models.CharField(default='N/A', max_length=200),
        ),
    ]
