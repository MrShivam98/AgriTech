# Generated by Django 4.0.4 on 2022-05-26 10:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.CharField(max_length=10)),
                ('time', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
        ),
    ]
