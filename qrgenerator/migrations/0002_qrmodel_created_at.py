# Generated by Django 3.1.5 on 2021-01-15 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrgenerator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='qrmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]