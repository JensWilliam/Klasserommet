# Generated by Django 5.1.2 on 2025-01-21 16:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_remove_topic_fag'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='fag',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='base.fag'),
            preserve_default=False,
        ),
    ]
