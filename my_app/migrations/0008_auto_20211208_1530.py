# Generated by Django 3.2.9 on 2021-12-08 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0007_auto_20211208_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='pincode',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='hr',
            name='pincode',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='manager',
            name='pincode',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='tester',
            name='pincode',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='developer',
            name='phone_number',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='hr',
            name='phone_number',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='manager',
            name='phone_number',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='tester',
            name='phone_number',
            field=models.CharField(max_length=10, null=True),
        ),
    ]