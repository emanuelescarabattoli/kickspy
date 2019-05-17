# Generated by Django 2.2.1 on 2019-05-17 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=512)),
                ('value', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Snapshot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=512)),
                ('date_time', models.CharField(max_length=512)),
                ('state_changed_at', models.CharField(max_length=512)),
                ('state', models.CharField(max_length=512)),
                ('backers_count', models.CharField(max_length=512)),
                ('pledged', models.CharField(max_length=512)),
                ('comments_count', models.CharField(max_length=512)),
                ('comments_for_display_count', models.CharField(max_length=512)),
            ],
        ),
    ]
