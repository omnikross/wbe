# Generated by Django 3.1 on 2020-08-29 20:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20200829_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='director',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, help_text='Unique ID of director', primary_key=True, serialize=False),
        ),
    ]
