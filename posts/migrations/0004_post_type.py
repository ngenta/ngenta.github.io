# Generated by Django 3.1.5 on 2021-07-09 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_comment_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='type',
            field=models.CharField(choices=[('general', 'general'), ('juveniles', 'general')], default='general', max_length=20),
        ),
    ]