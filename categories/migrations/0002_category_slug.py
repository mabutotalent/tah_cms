# Generated by Django 3.1 on 2020-09-08 04:30

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=True, editable=False, populate_from='title', unique=True),
        ),
    ]
