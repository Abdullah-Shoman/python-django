# Generated by Django 2.2.4 on 2024-04-06 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='comment',
            field=models.TextField(default='no comment'),
        ),
    ]
