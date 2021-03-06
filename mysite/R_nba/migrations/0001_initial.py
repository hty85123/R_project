# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-27 14:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Player_name', models.CharField(max_length=100)),
                ('Pos_name', models.CharField(max_length=100)),
                ('Height', models.CharField(max_length=100)),
                ('Weight', models.CharField(max_length=100)),
                ('Born', models.CharField(max_length=100)),
                ('Draft', models.CharField(max_length=100)),
                ('School', models.CharField(max_length=100)),
                ('Exp', models.CharField(max_length=100)),
                ('Photo_url', models.URLField()),
                ('Pos', models.IntegerField()),
                ('Active', models.IntegerField()),
                ('HoF', models.IntegerField()),
                ('All_Star', models.IntegerField()),
                ('All_Nba', models.IntegerField()),
                ('All_Def', models.IntegerField()),
                ('Score_Champ', models.IntegerField()),
                ('Assit_Champ', models.IntegerField()),
                ('Trb_Champ', models.IntegerField()),
                ('MVP', models.IntegerField()),
                ('GP', models.IntegerField()),
                ('PPG', models.FloatField()),
                ('TRPG', models.FloatField()),
                ('APG', models.FloatField()),
                ('BPG', models.FloatField()),
                ('SPG', models.FloatField()),
                ('PG_3', models.FloatField()),
                ('TP', models.IntegerField()),
                ('TR', models.IntegerField()),
                ('TAST', models.IntegerField()),
                ('TBLKS', models.IntegerField()),
                ('TSTLS', models.IntegerField()),
                ('TPS_3', models.IntegerField()),
                ('FG_percentage', models.FloatField()),
                ('FT_percentage', models.FloatField()),
                ('P3_percentage', models.FloatField()),
                ('EF_percentage', models.FloatField()),
                ('DRTG', models.IntegerField()),
                ('ORTG', models.IntegerField()),
                ('VORP', models.FloatField()),
                ('BPM', models.FloatField()),
                ('EFF', models.FloatField()),
                ('Win_Shares', models.FloatField()),
            ],
        ),
    ]
