# Generated by Django 4.0.5 on 2022-06-22 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sqlite3Exp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stuinfo',
            name='age',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]
