# Generated by Django 5.0 on 2023-12-21 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0008_rename_room_number_room_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='floor',
            name='name',
            field=models.PositiveIntegerField(),
        ),
    ]
