# Generated by Django 3.0.3 on 2020-08-21 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('f', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='document',
            field=models.FileField(null=True, upload_to='documents/%Y/%m/%d/'),
        ),
    ]
