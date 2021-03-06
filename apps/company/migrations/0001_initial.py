# Generated by Django 2.2.6 on 2019-10-15 21:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255, unique=True)),
                ('building_number', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=255)),
                ('locality', models.CharField(max_length=512)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='company.City')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='company.State')),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.State'),
        ),
    ]
