# Generated by Django 3.1 on 2020-08-06 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainPoll', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='name',
        ),
    ]
