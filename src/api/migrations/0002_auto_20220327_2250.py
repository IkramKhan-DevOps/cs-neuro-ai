# Generated by Django 3.2.12 on 2022-03-27 17:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='predication',
            options={'ordering': ['-id']},
        ),
        migrations.RemoveField(
            model_name='predication',
            name='age',
        ),
        migrations.RemoveField(
            model_name='predication',
            name='chest_pain_type',
        ),
        migrations.RemoveField(
            model_name='predication',
            name='cholestrol',
        ),
        migrations.RemoveField(
            model_name='predication',
            name='exercise_angina',
        ),
        migrations.RemoveField(
            model_name='predication',
            name='fasting_blood_sugar',
        ),
        migrations.RemoveField(
            model_name='predication',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='predication',
            name='max_heart_rate',
        ),
        migrations.RemoveField(
            model_name='predication',
            name='old_peak',
        ),
        migrations.RemoveField(
            model_name='predication',
            name='resting_bp_s',
        ),
        migrations.RemoveField(
            model_name='predication',
            name='resting_ecg',
        ),
        migrations.RemoveField(
            model_name='predication',
            name='st_slope',
        ),
        migrations.RemoveField(
            model_name='predication',
            name='target',
        ),
        migrations.AddField(
            model_name='predication',
            name='audio',
            field=models.FileField(default=django.utils.timezone.now, help_text='Please record voice [15sec-45sec]', upload_to='audios/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='predication',
            name='pitch',
            field=models.IntegerField(default=0),
        ),
    ]
