# Generated by Django 4.2.2 on 2023-07-03 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rfid_app', '0003_delete_rfidcard_tag_description_tag_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]