# Generated by Django 2.1.7 on 2019-10-06 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudApp', '0003_auto_20191006_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
    ]
