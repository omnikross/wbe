# Generated by Django 3.1 on 2020-08-29 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20200829_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]