# Generated by Django 3.0.6 on 2020-05-20 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
