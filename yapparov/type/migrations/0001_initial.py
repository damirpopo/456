# Generated by Django 4.1.4 on 2022-12-11 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('subtile', models.CharField(max_length=200)),
                ('URL', models.URLField(max_length=150)),
            ],
        ),
    ]
