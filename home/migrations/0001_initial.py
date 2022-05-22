# Generated by Django 4.0.4 on 2022-05-22 09:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=13)),
                ('content', models.TextField()),
                ('time', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='driver',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50, primary_key=True, serialize=False)),
                ('phone', models.CharField(max_length=13)),
                ('vehicle', models.CharField(max_length=10)),
                ('timeStamp', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='technology',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('title_url', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('iframe', models.CharField(max_length=300)),
                ('time', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='service',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('phone', models.CharField(max_length=13)),
                ('address', models.TextField(max_length=100)),
                ('weight', models.IntegerField()),
                ('timeStamp', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('driveby', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='driveby', to='home.driver')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
