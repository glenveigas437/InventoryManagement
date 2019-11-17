# Generated by Django 2.1.4 on 2019-11-12 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_name', models.CharField(max_length=100)),
                ('company', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('prod_type', models.CharField(max_length=100)),
                ('units', models.IntegerField()),
            ],
        ),
    ]
