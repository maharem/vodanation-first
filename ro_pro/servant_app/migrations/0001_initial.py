# Generated by Django 3.0.3 on 2020-08-25 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='general_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_id', models.CharField(max_length=30)),
                ('option', models.CharField(max_length=1)),
                ('region', models.CharField(choices=[('Alex', 'Alex'), ('Cairo', 'Cairo'), ('Delta', 'Delta'), ('Giza', 'Giza'), ('Upper', 'Upper')], max_length=30, null=True)),
                ('sub_region', models.CharField(max_length=30)),
                ('longitude', models.FloatField(blank=True, default=None, null=True)),
                ('latitude', models.FloatField(blank=True, default=None, null=True)),
                ('site_type', models.CharField(max_length=30)),
                ('structure_type', models.CharField(max_length=30)),
                ('cluster_avg', models.FloatField(blank=True, default=None, null=True)),
            ],
        ),
    ]
