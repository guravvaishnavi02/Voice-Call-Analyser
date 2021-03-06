# Generated by Django 3.2.8 on 2022-01-17 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0006_alter_audios_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio',
            fields=[
                ('audioid', models.AutoField(primary_key=True, serialize=False)),
                ('audio', models.FileField(upload_to='')),
                ('freqwrd', models.TextField()),
                ('tnscript', models.CharField(max_length=255)),
                ('diraize', models.FileField(upload_to='')),
                ('duration', models.FileField(upload_to='')),
                ('nospeaker', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('spid', models.AutoField(primary_key=True, serialize=False)),
                ('sp_audio', models.FileField(upload_to='')),
                ('sp_emo', models.FileField(upload_to='')),
                ('sp_emobar', models.FileField(upload_to='')),
                ('audioid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.audio')),
            ],
        ),
        migrations.DeleteModel(
            name='Audios',
        ),
    ]
