# Generated by Django 2.0.4 on 2018-04-08 21:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0003_auto_20180408_2129'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_type', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='propertie',
            name='home_type_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='properties.HomeType'),
        ),
    ]
