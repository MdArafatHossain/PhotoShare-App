# Generated by Django 3.1.6 on 2021-03-09 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20210308_1739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default='/default.jpg', upload_to=''),
        ),
    ]