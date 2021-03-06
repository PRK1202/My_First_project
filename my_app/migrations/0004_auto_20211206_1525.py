# Generated by Django 3.2.9 on 2021-12-06 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_alter_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='employee_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('dob', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('address', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('phone_number', models.BigIntegerField()),
                ('designamtion', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
    ]
