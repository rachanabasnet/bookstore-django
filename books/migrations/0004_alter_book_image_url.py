# Generated by Django 4.2.16 on 2024-12-03 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to='books'),
        ),
    ]
