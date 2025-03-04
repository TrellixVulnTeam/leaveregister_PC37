# Generated by Django 2.2.5 on 2019-10-13 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20191009_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='leaverequest',
            name='Days',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='emp_type',
            field=models.CharField(choices=[('Manager', 'Manager'), ('Hr', 'Hr'), ('Employee', 'Employee')], max_length=10),
        ),
        migrations.AlterField(
            model_name='leaverequest',
            name='ApplyTo',
            field=models.EmailField(choices=[('Manager', 'Manager'), ('Hr', 'Hr'), ('Admin', 'Admin')], default='', max_length=70),
        ),
    ]
