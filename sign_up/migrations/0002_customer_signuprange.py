# Generated by Django 2.1.7 on 2019-03-19 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sign_up', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Full name')),
                ('car', models.CharField(max_length=120, verbose_name='Make and model of car')),
                ('signup_date', models.DateField(verbose_name='Sign up time')),
                ('signup_time', models.CharField(max_length=5)),
                ('engeneer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sign_up.Engeneer')),
            ],
        ),
        migrations.CreateModel(
            name='SignUpRange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signup_time', models.CharField(max_length=5)),
            ],
        ),
    ]
