# Generated by Django 5.0.7 on 2024-07-15 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=23),
            preserve_default=False,
        ),
    ]
