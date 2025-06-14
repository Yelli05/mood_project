# Generated by Django 5.2.1 on 2025-06-03 11:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodpicker', '0002_food_mood_alter_food_name'),
        ('moods', '0003_mood_emoji'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='mood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='moods.mood'),
        ),
    ]
