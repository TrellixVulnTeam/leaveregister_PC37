# Generated by Django 2.2.5 on 2019-10-13 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_remove_leaverequest_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaverequest',
            name='From',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='leaverequest',
            name='To',
            field=models.DateTimeField(),
        ),
    ]
