# Generated by Django 5.0.4 on 2024-04-07 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0011_livro_in_collection_livro_in_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='in_collection',
            field=models.BooleanField(default=True),
        ),
    ]