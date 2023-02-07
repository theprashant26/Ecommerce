# Generated by Django 3.2.9 on 2022-11-10 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ehome', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactform',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=40, null=True)),
                ('phone', models.IntegerField(null=True)),
                ('email', models.EmailField(max_length=30, null=True)),
                ('message', models.TextField(max_length=300, null=True)),
            ],
        ),
    ]
