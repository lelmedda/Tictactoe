# Generated by Django 3.2.6 on 2021-10-13 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='move',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='board',
            field=models.CharField(blank=True, max_length=9),
        ),
    ]
