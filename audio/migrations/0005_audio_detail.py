# Generated by Django 2.1 on 2018-10-25 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0004_auto_20181023_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Audio_Detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_title', models.CharField(max_length=20)),
                ('detail_author', models.CharField(max_length=20)),
                ('detail_translator', models.CharField(blank=True, max_length=20, null=True)),
                ('detail_speaker', models.CharField(max_length=20)),
                ('detail_pubdate', models.DateTimeField(blank=True, null=True)),
                ('detail_text', models.TextField()),
                ('detail_imgsrc', models.CharField(max_length=255)),
                ('detail_playtime', models.TimeField(blank=True)),
                ('detail_filesize', models.CharField(max_length=20, null=True)),
                ('detail_price', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
                ('detail_outline', models.TextField()),
                ('detail_parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audio.Audio')),
            ],
        ),
    ]
