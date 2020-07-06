# Generated by Django 3.0.8 on 2020-07-06 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('capital', models.CharField(max_length=20)),
                ('slug', models.SlugField(max_length=21)),
            ],
        ),
        migrations.CreateModel(
            name='LocalGovernmentArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('state', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lgas', to='states.State')),
            ],
        ),
    ]
