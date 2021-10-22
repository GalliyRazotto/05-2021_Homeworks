# Generated by Django 3.2.8 on 2021-10-22 19:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacture',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.CharField(default='', max_length=64)),
                ('carManufacture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cars.manufacture')),
            ],
        ),
    ]
