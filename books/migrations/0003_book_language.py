# Generated by Django 4.2.16 on 2024-12-03 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
