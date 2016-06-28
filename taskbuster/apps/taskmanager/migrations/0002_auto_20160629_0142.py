# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('taskmanager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='name', help_text='Enter the project name', max_length=100)),
                ('color', models.CharField(verbose_name='color', validators=[django.core.validators.RegexValidator('(^#[0-9a-fA-F]{3}$)|(^#[0-9a-fA-F]{6}$)')], help_text='Enter the hex color code, like #ccc or #cccccc', default='#fff', max_length=7)),
                ('user', models.ForeignKey(to='taskmanager.Profile', verbose_name='user', related_name='projects')),
            ],
            options={
                'verbose_name': 'Project',
                'ordering': ('user', 'name'),
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.AlterUniqueTogether(
            name='project',
            unique_together=set([('user', 'name')]),
        ),
    ]
