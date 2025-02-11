# Generated by Django 5.1.2 on 2025-01-21 16:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_profile_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('laerer', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='topic',
            name='fag',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='topics', to='base.fag'),
            preserve_default=False,
        ),
    ]
