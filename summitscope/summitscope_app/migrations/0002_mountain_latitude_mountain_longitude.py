# Generated by Django 5.0.3 on 2024-04-02 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summitscope_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mountain',
            name='latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='mountain',
            name='longitude',
            field=models.FloatField(default=0.0),
        ),
    ]