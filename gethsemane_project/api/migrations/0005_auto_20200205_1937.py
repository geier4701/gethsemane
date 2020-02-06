# Generated by Django 3.0.2 on 2020-02-06 01:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200201_1201'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subroutinemodel',
            old_name='ship_id',
            new_name='ship',
        ),
        migrations.AddField(
            model_name='actionmodel',
            name='subroutines',
            field=models.ManyToManyField(to='api.SubroutineModel'),
        ),
        migrations.AddField(
            model_name='conditionmodel',
            name='component_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='conditionmodel',
            name='component_type',
            field=models.CharField(blank=True, choices=[('AT', 'AmmunitionType'), ('AR', 'Armour'), ('CO', 'Computer'), ('IE', 'ImpulseEngine'), ('JD', 'JumpDrive'), ('RA', 'Radar'), ('WE', 'Weapon')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='conditionmodel',
            name='subroutine',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.SubroutineModel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shipmodel',
            name='name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shipmodel',
            name='ship_type',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='api.ShipTypeModel'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='conditionmodel',
            name='at_least',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='conditionmodel',
            name='at_most',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
