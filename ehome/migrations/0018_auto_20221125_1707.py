# Generated by Django 3.2.9 on 2022-11-25 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ehome', '0017_alter_product_product_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
