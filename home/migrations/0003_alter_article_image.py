# Generated by Django 4.0.4 on 2022-05-26 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.CharField(max_length=50),
        ),
    ]
