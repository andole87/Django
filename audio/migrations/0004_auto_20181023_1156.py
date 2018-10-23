# Generated by Django 2.1 on 2018-10-23 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0003_audio_imgsrc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='speaker',
            field=models.CharField(db_index=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='audio',
            name='title',
            field=models.CharField(db_index=True, max_length=20),
        ),
    ]