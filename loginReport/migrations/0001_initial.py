# Generated by Django 3.2.4 on 2021-06-28 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
                ('ip_address', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=30)),
                ('user_agent', models.CharField(max_length=50)),
                ('cookie', models.CharField(max_length=10000)),
                ('referer', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
    ]
