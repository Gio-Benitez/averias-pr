# Generated by Django 5.0.3 on 2024-03-11 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='municipality',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('population', models.IntegerField()),
                ('area_size', models.DecimalField(decimal_places=5, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('status', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='report_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line_1', models.CharField(max_length=255)),
                ('address_line_2', models.CharField(max_length=255)),
                ('category', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('zipcode', models.CharField(max_length=5)),
                ('geo_data_lat', models.DecimalField(decimal_places=5, max_digits=5)),
                ('geo_data_long', models.DecimalField(decimal_places=5, max_digits=5)),
                ('image', models.ImageField(upload_to=None)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
    ]
