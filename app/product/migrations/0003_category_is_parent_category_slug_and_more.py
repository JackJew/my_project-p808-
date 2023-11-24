# Generated by Django 4.2.7 on 2023-11-23 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_category_child'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_parent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.RemoveField(
            model_name='category',
            name='child',
        ),
        migrations.AddField(
            model_name='category',
            name='child',
            field=models.ManyToManyField(blank=True, to='product.category'),
        ),
    ]