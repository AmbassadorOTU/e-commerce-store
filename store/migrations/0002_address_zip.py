# Generated by Django 4.1 on 2022-08-21 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='zip',
            field=models.CharField(default=0, max_length=255),
            preserve_default=False,
        ),
    ]