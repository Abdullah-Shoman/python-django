# Generated by Django 2.2.4 on 2024-04-03 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_show_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='description',
            field=models.TextField(default='old'),
            preserve_default=False,
        ),
    ]
