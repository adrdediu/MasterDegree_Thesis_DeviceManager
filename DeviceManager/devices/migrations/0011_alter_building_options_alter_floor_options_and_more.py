# Generated by Django 5.0 on 2023-12-22 14:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devices', '0010_alter_floor_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='building',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='floor',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='room',
            options={'ordering': ['id']},
        ),
        migrations.AddField(
            model_name='device',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='device',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='device',
            name='serial_number',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
