# Generated by Django 2.2.4 on 2024-03-29 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_and_authors_app', '0002_book_authors'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default='old notes'),
            preserve_default=False,
        ),
    ]