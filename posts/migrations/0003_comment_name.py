# Generated by Django 3.1.5 on 2021-01-24 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_comment_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.TextField(default='elsuperhincha'),
            preserve_default=False,
        ),
    ]
