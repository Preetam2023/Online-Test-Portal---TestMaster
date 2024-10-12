# Generated by Django 5.1.2 on 2024-10-12 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_remove_question_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='option_1',
        ),
        migrations.RemoveField(
            model_name='question',
            name='option_2',
        ),
        migrations.RemoveField(
            model_name='question',
            name='option_3',
        ),
        migrations.RemoveField(
            model_name='question',
            name='option_4',
        ),
        migrations.AddField(
            model_name='question',
            name='options',
            field=models.JSONField(default=list),
        ),
        migrations.AlterField(
            model_name='question',
            name='difficulty',
            field=models.CharField(max_length=10),
        ),
    ]
