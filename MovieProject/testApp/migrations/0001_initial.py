# Generated by Django 2.2.12 on 2020-04-06 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rdate', models.IntegerField()),
                ('moviename', models.CharField(max_length=30)),
                ('hero', models.CharField(max_length=30)),
                ('heroine', models.CharField(max_length=30)),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
