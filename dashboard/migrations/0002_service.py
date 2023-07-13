# Generated by Django 3.2 on 2023-07-13 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='services')),
                ('title', models.CharField(max_length=100)),
                ('car_type', models.CharField(blank=True, max_length=100, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('time', models.CharField(blank=True, max_length=100, null=True)),
                ('service_name', models.CharField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('s_from', models.CharField(blank=True, max_length=100, null=True)),
                ('s_to', models.CharField(blank=True, max_length=100, null=True)),
                ('menu', models.CharField(choices=[('Hourly Car Rental', 'Hourly Car Rental'), ('Daily Basis Rent A Car - Inside Dhaka', 'Daily Basis Rent A Car - Inside Dhaka'), ('Daily Basis Rent A Car - Outside Dhaka', 'Daily Basis Rent A Car - Outside Dhaka'), ('Monthly Car Rental', 'Monthly Car Rental'), ('Office Pick & Drop', 'Office Pick & Drop'), ('Inter District Pick&amp', 'Inter District Pick&amp'), ('Rent A Car in Sylhet', 'Rent A Car in Sylhet'), ('Rent A Car in Chittagong', 'Rent A Car in Chittagong'), ('Rent A Car in Cox s Bazar', 'Rent A Car in Cox s Bazar'), ('Rent A Car in Sajek Khagrachari', 'Rent A Car in Sajek Khagrachari'), ('Tour Package', 'Tour Package')], max_length=255)),
            ],
        ),
    ]