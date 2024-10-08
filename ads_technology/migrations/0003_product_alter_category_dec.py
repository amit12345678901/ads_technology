# Generated by Django 5.1.1 on 2024-09-24 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads_technology', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='products/')),
                ('original_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discounted_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('review_count', models.PositiveIntegerField()),
                ('discount_percentage', models.PositiveIntegerField()),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='dec',
            field=models.CharField(max_length=150, verbose_name='Description'),
        ),
    ]
