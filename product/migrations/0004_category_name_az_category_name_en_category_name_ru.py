# Generated by Django 4.2.7 on 2023-11-26 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_category_is_parent_category_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_az',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_en',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
