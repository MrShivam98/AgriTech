# Generated by Django 4.0.3 on 2022-03-12 20:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_service_pincode'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='completed',
        ),
        migrations.AddField(
            model_name='service',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
