# Generated by Django 2.1.2 on 2018-11-09 22:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='userBlocked', to=settings.AUTH_USER_MODEL)),
                ('userBlocking', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='userBlocking', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('document', models.FileField(upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isRequest', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='userFollowed', to=settings.AUTH_USER_MODEL)),
                ('userFollowing', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='userFollowing', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('messageContent', models.TextField()),
                ('datePosted', models.DateTimeField(auto_now_add=True)),
                ('isRequest', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('postContent', models.TextField()),
                ('datePosted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField()),
                ('age', models.PositiveIntegerField()),
                ('photo', models.ImageField(null=True, upload_to='profile_photos/')),
                ('location', models.CharField(blank=True, default='', max_length=150)),
                ('latitude', models.FloatField(default=0.0, max_length=150)),
                ('longitude', models.FloatField(default=0.0, max_length=150)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ResetURL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, max_length=255)),
                ('timeStamp', models.DateTimeField(auto_now_add=True)),
                ('isValid', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userOne', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userOne', to=settings.AUTH_USER_MODEL)),
                ('userTwo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userTwo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='pages.Profile'),
        ),
        migrations.AddField(
            model_name='message',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.Thread'),
        ),
    ]