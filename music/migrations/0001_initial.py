# Generated by Django 4.1.5 on 2023-03-02 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='audio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('size', models.FloatField()),
                ('upload_date', models.DateField()),
                ('language', models.CharField(max_length=50)),
                ('duration', models.DurationField()),
                ('thumbnail', models.ImageField(upload_to='images/')),
                ('audio_file', models.FileField(upload_to='audio/')),
                ('description', models.TextField(max_length=100)),
                ('type', models.CharField(max_length=20)),
                ('artist', models.TextField(max_length=50)),
            ],
        ),
    ]
