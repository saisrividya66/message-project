# Generated by Django 4.2.5 on 2023-10-03 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friend_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='msg',
            old_name='mobile',
            new_name='mobile',
        ),
        migrations.AlterField(
            model_name='msg',
            name='msg',
            field=models.CharField(max_length=200),
        ),
    ]
