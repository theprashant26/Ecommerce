# Generated by Django 4.1.4 on 2023-02-06 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ehome', '0019_alter_orderplaced_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On the way', 'On the way'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel')], default='Pending', max_length=60),
        ),
    ]
