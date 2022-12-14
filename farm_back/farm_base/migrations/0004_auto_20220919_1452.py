# Generated by Django 2.2 on 2022-09-19 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farm_base', '0003_farm_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farm',
            name='municipality',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Municipality'),
        ),
        migrations.AlterField(
            model_name='farm',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='farm',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='farm_base.Owner'),
        ),
        migrations.AlterField(
            model_name='farm',
            name='state',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='State'),
        ),
    ]
