# Generated by Django 3.1.7 on 2021-07-23 21:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscribe', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='email',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='price',
        ),
    ]
