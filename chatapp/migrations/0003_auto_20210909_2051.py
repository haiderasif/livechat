# Generated by Django 3.2.6 on 2021-09-09 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0002_messages'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Messages',
            new_name='Message',
        ),
        migrations.RenameField(
            model_name='message',
            old_name='message',
            new_name='value',
        ),
    ]