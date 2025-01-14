# Generated by Django 5.1.4 on 2024-12-06 07:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('painting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=200, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('date_joined', models.DateField(auto_now_add=True)),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=200)),
                ('nickname', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('is_gallery', models.BooleanField(default=False)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='profile_pictures/')),
                ('Theme', models.CharField(blank=True, max_length=255, null=True)),
                ('Dark_light_theme', models.CharField(blank=True, max_length=255, null=True)),
                ('favorite_painter', models.CharField(blank=True, max_length=255, null=True)),
                ('favorite_painting', models.CharField(blank=True, max_length=255, null=True)),
                ('favorite_painting_style', models.CharField(blank=True, max_length=255, null=True)),
                ('favorite_painting_technique', models.CharField(blank=True, max_length=255, null=True)),
                ('favorite_painting_to_own', models.CharField(blank=True, max_length=255, null=True)),
                ('biography', models.TextField(blank=True, null=True)),
                ('gallery_name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('number_of_paintings', models.IntegerField(default=0)),
                ('number_of_artists', models.IntegerField(default=0)),
                ('cover_painting', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='galleries_as_cover', to='painting.painting')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
