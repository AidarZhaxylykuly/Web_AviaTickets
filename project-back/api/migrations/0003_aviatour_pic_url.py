# Generated by Django 5.0.4 on 2024-04-17 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_hotel_alter_reservation_total_cost_reservation_hotel'),
    ]

    operations = [
        migrations.AddField(
            model_name='aviatour',
            name='pic_url',
            field=models.CharField(default=None, max_length=500),
            preserve_default=False,
        ),
    ]
