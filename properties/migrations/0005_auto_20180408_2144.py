# Generated by Django 2.0.4 on 2018-04-08 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_auto_20180408_2132'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='propertie',
            options={'verbose_name': 'Property', 'verbose_name_plural': 'Properties'},
        ),
        migrations.AlterField(
            model_name='propertie',
            name='home_type_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='properties.HomeType', verbose_name='Home Type'),
        ),
    ]
