# Generated by Django 3.1.5 on 2021-01-23 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default='2020-10-29'),
            preserve_default=False,
        ),
    ]
