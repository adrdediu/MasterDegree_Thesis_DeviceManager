# Generated by Django 5.0.1 on 2024-07-14 11:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0014_device_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventorizationroom',
            name='inventorization',
        ),
        migrations.RemoveField(
            model_name='inventorizationroom',
            name='room',
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.building')),
            ],
        ),
        migrations.DeleteModel(
            name='InventorizationDevice',
        ),
        migrations.DeleteModel(
            name='InventorizationRoom',
        ),
    ]