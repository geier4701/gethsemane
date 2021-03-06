# Generated by Django 3.0.2 on 2020-04-09 20:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0008_auto_20200329_1620'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharacterModel',
            fields=[
                ('character_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='ammunitionmodel',
            name='characters',
            field=models.ManyToManyField(to='api.CharacterModel'),
        ),
        migrations.AddField(
            model_name='armourmodel',
            name='characters',
            field=models.ManyToManyField(to='api.CharacterModel'),
        ),
        migrations.AddField(
            model_name='computermodel',
            name='characters',
            field=models.ManyToManyField(to='api.CharacterModel'),
        ),
        migrations.AddField(
            model_name='impulseenginemodel',
            name='characters',
            field=models.ManyToManyField(to='api.CharacterModel'),
        ),
        migrations.AddField(
            model_name='jumpdrivemodel',
            name='characters',
            field=models.ManyToManyField(to='api.CharacterModel'),
        ),
        migrations.AddField(
            model_name='radarmodel',
            name='characters',
            field=models.ManyToManyField(to='api.CharacterModel'),
        ),
        migrations.AddField(
            model_name='shipmodel',
            name='character',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.CharacterModel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shiptypemodel',
            name='characters',
            field=models.ManyToManyField(to='api.CharacterModel'),
        ),
        migrations.AddField(
            model_name='weaponmodel',
            name='characters',
            field=models.ManyToManyField(to='api.CharacterModel'),
        ),
    ]
