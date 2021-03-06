# Generated by Django 3.0.3 on 2020-08-24 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActVals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_taken', models.CharField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='BuilVals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building', models.CharField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='ConsVals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consultant_name', models.CharField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='ReqVals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requester_dept', models.CharField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='SiteInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_id', models.CharField(max_length=256)),
                ('email_address', models.CharField(default='', max_length=256)),
                ('staff_id', models.CharField(default='', max_length=256)),
                ('area', models.CharField(default='', max_length=256)),
                ('rt_gf', models.CharField(default='', max_length=256)),
                ('str_type', models.CharField(default='', max_length=256)),
                ('height', models.CharField(default='', max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='SiteVals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_case', models.CharField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='StarVals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star_site', models.CharField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='StatVals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(blank=True, max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='SiteData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_id', models.CharField(max_length=256)),
                ('remarks', models.CharField(default='', max_length=256)),
                ('mail_name', models.CharField(default='', max_length=256)),
                ('project_name', models.CharField(default='', max_length=256)),
                ('max_rating_in', models.CharField(default='', max_length=256)),
                ('consultant_recommendations', models.CharField(default='', max_length=256)),
                ('new_requirement', models.TextField(default='')),
                ('request_date', models.DateField(default='2020-08-24')),
                ('last_visit', models.DateField(default='2020-08-24')),
                ('feedback', models.DateField(default='2020-08-24')),
                ('max_rating_per', models.FloatField(default='0.1', max_length=256)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('in_progress_date', models.CharField(blank=True, max_length=256)),
                ('done_date', models.CharField(blank=True, max_length=256)),
                ('email_address', models.CharField(default='', max_length=256)),
                ('staff_id', models.CharField(default='', max_length=256)),
                ('area', models.CharField(default='', max_length=256)),
                ('rt_gf', models.CharField(default='', max_length=256)),
                ('str_type', models.CharField(default='', max_length=256)),
                ('height', models.CharField(default='', max_length=256)),
                ('action_taken', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='ro_app.ActVals')),
                ('building', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='ro_app.BuilVals')),
                ('consultant_name', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='ro_app.ConsVals')),
                ('requester_dept', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='ro_app.ReqVals')),
                ('site_case', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='ro_app.SiteVals')),
                ('star_site', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='ro_app.StarVals')),
                ('status', models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='ro_app.StatVals')),
            ],
        ),
    ]
