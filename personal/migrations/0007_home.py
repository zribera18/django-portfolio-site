# Generated by Django 2.0.6 on 2018-07-24 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0006_auto_20180703_1052'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
            ],
        ),
    ]
