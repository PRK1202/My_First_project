# Generated by Django 3.2.9 on 2021-12-03 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
