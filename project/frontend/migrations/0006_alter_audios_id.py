# Generated by Django 3.2.8 on 2022-01-17 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_auto_20220117_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audios',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]