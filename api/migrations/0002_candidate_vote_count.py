# Generated by Django 4.1.7 on 2023-06-06 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='vote_count',
            field=models.IntegerField(default=0),
        ),
    ]