# Generated by Django 3.2.4 on 2021-06-24 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='text',
            field=models.CharField(default='', max_length=100),
        ),
    ]
