# Generated by Django 4.1.7 on 2023-05-12 19:04

import api.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(db_index=True, max_length=255, unique=True)),
                ('email', models.EmailField(db_index=True, max_length=255, unique=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_name', models.CharField(max_length=100)),
                ('party', models.CharField(max_length=50)),
                ('candidate_image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Election',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('election_name', models.CharField(max_length=100)),
                ('election_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Imagerec',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
                ('cover', models.ImageField(blank=True, null=True, upload_to=api.models.upload_path)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('candidate_foreign', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.candidate')),
                ('election_foreign', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.election')),
            ],
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actual_name', models.CharField(blank=True, max_length=200, null=True)),
                ('mobile_number', models.CharField(blank=True, max_length=200, null=True)),
                ('voters_id', models.CharField(blank=True, max_length=100, null=True)),
                ('adhar_number', models.CharField(blank=True, max_length=100, null=True)),
                ('pan_number', models.CharField(blank=True, max_length=100, null=True)),
                ('user_image', models.ImageField(blank=True, null=True, upload_to='user_images')),
                ('user_foreign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='election',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.election'),
        ),
    ]
