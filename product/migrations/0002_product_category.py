# Generated by Django 4.2.2 on 2023-06-14 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_alter_category_image'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(to='categories.category'),
        ),
    ]
