# Generated by Django 2.1 on 2018-10-26 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0007_auto_20181026_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='title_author',
            field=models.CharField(default='미상', max_length=5),
            preserve_default=False,
        ),
    ]