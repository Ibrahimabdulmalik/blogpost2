# Generated by Django 2.2.6 on 2020-06-08 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Designer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('country_of_origin', models.CharField(max_length=64)),
                ('state_of_origin', models.CharField(max_length=64)),
                ('slug', models.SlugField(default='designer', unique=True)),
            ],
            options={
                'ordering': ['-name', '-specialty', '-slug'],
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Posture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style_name', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('description', models.TextField()),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('likes', models.IntegerField(default=0)),
                ('dislikes', models.IntegerField(default=0)),
                ('designer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fashblog.Designer')),
            ],
        ),
        migrations.AddField(
            model_name='designer',
            name='specialty',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fashblog.Gender'),
        ),
    ]