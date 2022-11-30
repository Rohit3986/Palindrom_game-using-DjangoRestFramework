# Generated by Django 3.2.16 on 2022-11-29 15:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0005_alter_game_string'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='player',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='game',
            name='string',
            field=models.CharField(blank=True, default='', editable=False, max_length=6),
        ),
        migrations.DeleteModel(
            name='asdd',
        ),
    ]
