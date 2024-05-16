# Generated by Django 4.0.5 on 2022-08-12 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farmsystem', '0009_alter_event_activities_id_alter_event_batch_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_order_request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('harvest_id', models.IntegerField()),
                ('plant_name', models.CharField(max_length=200)),
                ('grade', models.CharField(max_length=200)),
                ('quantity', models.CharField(max_length=200)),
                ('units', models.CharField(max_length=200)),
                ('date_needed', models.CharField(max_length=200)),
                ('is_admin_approved', models.BooleanField(default=False)),
                ('desc', models.CharField(max_length=200)),
                ('user_id', models.ForeignKey(db_constraint=False, default=1, on_delete=django.db.models.deletion.CASCADE, to='farmsystem.user_account')),
            ],
        ),
    ]
