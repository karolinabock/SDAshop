# Generated by Django 3.1.7 on 2021-03-07 11:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('country_of_origin', models.CharField(default=None, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('brand_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SDAshop.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('year_of_production', models.IntegerField(default=0)),
                ('engine', models.CharField(max_length=50)),
                ('gear_box', models.CharField(choices=[('manual', 'Manual'), ('automatic', 'Automatic')], default='', max_length=30)),
                ('new_or_used', models.CharField(choices=[('new', 'New'), ('used', 'Used')], default='', max_length=30)),
                ('body_type', models.CharField(choices=[('convertible', 'Convertible'), ('coupe', 'Coupe'), ('minivan', 'Minivan'), ('sedan', 'Sedan'), ('suv', 'Suv'), ('wagon', 'Wagon')], default='', max_length=30)),
                ('fuel_type', models.CharField(choices=[('diesel', 'Diesel'), ('gasoline', 'Gasoline')], default='', max_length=30)),
                ('color', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
                ('in_stock', models.BooleanField(default=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('brand_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SDAshop.brand')),
                ('car_model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SDAshop.carmodel')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_creator', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
