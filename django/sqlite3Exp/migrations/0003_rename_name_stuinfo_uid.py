# Generated by Django 4.0.5 on 2022-06-23 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sqlite3Exp', '0002_alter_stuinfo_age'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stuinfo',
            old_name='name',
            new_name='UID',
        ),
    ]
