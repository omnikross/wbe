# Generated by Django 3.1 on 2020-08-29 16:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20200828_1940'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='filminstance',
            options={'ordering': ['session_time']},
        ),
        migrations.RemoveField(
            model_name='filminstance',
            name='due_back',
        ),
        migrations.AddField(
            model_name='filminstance',
            name='session_time',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='filminstance',
            name='status',
            field=models.CharField(blank=True, choices=[('s', 'Sold'), ('a', 'Available'), ('r', 'Reserved')], default='m', help_text='Film availability', max_length=25),
        ),
    ]
