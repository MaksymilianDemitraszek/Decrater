# Generated by Django 2.1.3 on 2018-11-18 01:16

from django.db import migrations, models
import django.db.models.deletion
import pathLogger.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PathBlock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deviceId', models.TextField()),
                ('timestampStart', models.BigIntegerField()),
                ('timestampEnd', models.BigIntegerField()),
                ('latStart', models.FloatField()),
                ('lngStart', models.FloatField()),
                ('latEnd', models.FloatField()),
                ('lngEnd', models.FloatField()),
            ],
            managers=[
                ('objects', pathLogger.models.PathBlockManager()),
            ],
        ),
        migrations.CreateModel(
            name='QuakeDelta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.FloatField()),
                ('y', models.FloatField()),
                ('z', models.FloatField()),
            ],
        ),
        migrations.AddField(
            model_name='pathblock',
            name='quakeDelta',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='pathLogger.QuakeDelta'),
        ),
    ]
