# Generated by Django 3.1.5 on 2021-01-13 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20210113_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='vote',
            field=models.IntegerField(default=0, editable=False),
        ),
    ]