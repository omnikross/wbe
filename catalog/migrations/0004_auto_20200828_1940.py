# Generated by Django 3.1 on 2020-08-28 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20200828_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='avatar',
            field=models.CharField(default='default.png', help_text='Select by name image of your film', max_length=100),
        ),
        migrations.DeleteModel(
            name='FilmImage',
        ),
    ]
