# Generated by Django 3.1.5 on 2021-07-10 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='competicion',
            field=models.ImageField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.CharField(choices=[('general', 'general'), ('juveniles', 'juveniles')], default='general', max_length=20),
        ),
    ]