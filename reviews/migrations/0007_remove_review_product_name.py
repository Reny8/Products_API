# Generated by Django 4.0.3 on 2022-04-04 14:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0006_alter_review_product_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='product_name',
        ),
    ]
