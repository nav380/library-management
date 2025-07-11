# Generated by Django 5.2 on 2025-05-09 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='available_copies',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='book',
            name='numberofcopies',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='book',
            name='serial_number',
            field=models.CharField(default='', max_length=255, unique=True),
        ),
    ]
