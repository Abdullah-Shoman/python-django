# Generated by Django 2.2.4 on 2024-03-29 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_and_authors_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(related_name='books', to='books_and_authors_app.Author'),
        ),
    ]
