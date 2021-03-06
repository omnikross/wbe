# Generated by Django 3.1 on 2020-08-28 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20200827_2234'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilmImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a film image name (e.g. Avatar part 1 image . (png/jpg), without spaces.)', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='film',
            name='avatar',
            field=models.OneToOneField(help_text='Select by name image of your film', null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.filmimage'),
        ),
    ]
