# Generated by Django 2.1.2 on 2018-10-29 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maintenance', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show', models.TextField(default='')),
                ('season', models.IntegerField(default=1)),
                ('episode', models.IntegerField(default=1)),
                ('quality', models.TextField(default='0p')),
                ('url', models.URLField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=1000)),
                ('noof', models.BigIntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='videos',
            name='website',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mains.website'),
        ),
    ]
