# Generated by Django 3.2.9 on 2022-11-16 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ehome', '0007_cart_orderplaced_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_avail',
            field=models.FloatField(default=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('F&V', 'Fruits & Vegetables'), ('G&S', 'Grocery & Staples'), ('Bev', 'Beverages'), ('H&K', 'Home & Kitchen'), ('B&D', 'Breakfast & Dairy'), ('B,S&C', 'Biscuits, Snacks & Chocolates'), ('N,S&I_F', 'Noodles, Sauces & Instant Food'), ('M,F&S', 'Meats, Frozen & Seafood')], max_length=20),
        ),
    ]