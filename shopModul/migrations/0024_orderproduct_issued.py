# Generated by Django 4.2 on 2023-09-23 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopModul', '0023_alter_clientinfo_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderproduct',
            name='issued',
            field=models.BooleanField(default=False),
        ),
    ]
