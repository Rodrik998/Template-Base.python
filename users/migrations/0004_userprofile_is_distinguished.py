# Generated by Django 4.1.7 on 2023-05-04 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_userprofile_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_distinguished',
            field=models.BooleanField(default=False),
        ),
    ]
