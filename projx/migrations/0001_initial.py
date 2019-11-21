# Generated by Django 2.2.7 on 2019-11-19 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('image', models.ImageField(upload_to='poster')),
                ('description', models.TextField()),
                ('language', models.CharField(max_length=20)),
                ('director', models.CharField(max_length=30)),
                ('release', models.DateField()),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('image', models.ImageField(upload_to='poster')),
                ('discription', models.TextField()),
                ('rating', models.FloatField()),
                ('language', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('s_series', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projx.Series')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=100)),
                ('g_movie', models.ManyToManyField(blank=True, to='projx.Movies')),
                ('g_series', models.ManyToManyField(blank=True, to='projx.Series')),
            ],
        ),
        migrations.CreateModel(
            name='Episode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('length', models.TimeField()),
                ('description', models.TextField()),
                ('rating', models.FloatField()),
                ('release', models.DateField()),
                ('e_season', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projx.Season')),
            ],
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('profile', models.ImageField(upload_to='profile')),
                ('gender', models.CharField(max_length=10)),
                ('dob', models.DateField()),
                ('movie', models.ManyToManyField(blank=True, to='projx.Movies')),
                ('series', models.ManyToManyField(blank=True, to='projx.Series')),
            ],
        ),
    ]
