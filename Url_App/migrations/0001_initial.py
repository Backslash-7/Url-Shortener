# Generated by Django 3.2.6 on 2021-10-02 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Url',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Your_url', models.CharField(max_length=500, unique=True)),
                ('short_url', models.CharField(max_length=20, unique=True)),
            ],
        ),
    ]
