# Generated by Django 5.1.2 on 2024-10-12 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='option_1',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='option_2',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='option_3',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='option_4',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
