# Generated by Django 3.1.6 on 2021-03-08 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210308_1712'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='pic_url',
        ),
    ]
