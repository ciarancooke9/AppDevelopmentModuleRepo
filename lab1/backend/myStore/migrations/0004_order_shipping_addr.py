# Generated by Django 2.2.12 on 2022-10-03 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myStore', '0003_auto_20220920_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipping_addr',
            field=models.TextField(default=''),
        ),
    ]
