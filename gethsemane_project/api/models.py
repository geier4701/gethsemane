from django.db import models


class ImpulseEngineModel(models.Model):
	impulse_engine_id = models.AutoField(primary_key=True, unique=True)
	name = models.CharField(max_length=100, unique=True)
	mass = models.IntegerField()
	energy_cost = models.IntegerField()
	repair_cost = models.IntegerField()
	max_accel = models.IntegerField()


class JumpDriveModel(models.Model):
	jump_drive_id = models.AutoField(primary_key=True, unique=True)
	name = models.CharField(max_length=100, unique=True)
	mass = models.IntegerField()
	energy_cost = models.IntegerField()
	repair_cost = models.IntegerField()


class WeaponModel(models.Model):
	weapon_id: models.AutoField(primary_key=True, unique=True)
	name = models.CharField(max_length=100, unique=True)
	mass = models.IntegerField()
	energy_cost = models.IntegerField()
	repair_cost = models.IntegerField()
	damage = models.IntegerField()
	munition_velocity = models.IntegerField()
	ammunition_type = models.IntegerField(choices=[(0, 'CRYSTAL'), (1, 'MISSILE'), (2, 'RAIL'), (3, 'ELECTRIC')])


class RadarModel(models.Model):
	radar_id = models.AutoField(primary_key=True, unique=True)
	name = models.CharField(max_length=100, unique=True)
	mass = models.IntegerField()
	energy_cost = models.IntegerField()
	repair_cost = models.IntegerField()
	tracking_style = models.IntegerField(choices=[(0, 'PASSIVE'), (1, 'ACTIVE')])


class ArmourModel(models.Model):
	armour_id = models.AutoField(primary_key=True, unique=True)
	name = models.CharField(max_length=100, unique=True)
	mass = models.IntegerField()
	repair_cost = models.IntegerField()
	armour_type = models.IntegerField(choices=[(0, 'REFLECTIVE'), (1, 'REACTIVE'), (2, 'ABLATIVE'), (3, 'CHARGED')])


class ShipTypeModel(models.Model):
	ship_type_id = models.AutoField(primary_key=True, unique=True)
	name = models.CharField(max_length=100, unique=True)
	weight = models.IntegerField()
	power_gen = models.IntegerField()
	battery_max = models.IntegerField()
	health = models.IntegerField()


# ADD COUNT ON AMMUNITION_SHIP BRIDGE TABLE
class AmmunitionModel(models.Model):
	ammunition_id = models.AutoField(primary_key=True, unique=True)
	name = models.CharField(max_length=100, unique=True)
	mass = models.IntegerField()
	repair_cost = models.IntegerField()
	damage_type = models.IntegerField(choices=[(0, 'ENERGY'), (1, 'EXPLOSIVE'), (2, 'IMPACT'), (3, 'EWAR')])
	ammunition_type = models.IntegerField(choices=[(0, 'CRYSTAL'), (1, 'MISSILE'), (2, 'RAIL'), (3, 'ELECTRIC')])
	max_ammunition = models.IntegerField()


class ComputerModel(models.Model):
	computer_id = models.AutoField(primary_key=True, unique=True)
	name = models.CharField(max_length=100, unique=True)
	mass = models.IntegerField()
	repair_cost = models.IntegerField()
	speed = models.IntegerField()
	capacity = models.IntegerField()


class ShipModel(models.Model):
	ship_id = models.AutoField(primary_key=True, unique=True)
	name = models.CharField(max_length=100)
	radar = models.ForeignKey(RadarModel, on_delete=models.CASCADE)
	jump_drive = models.ForeignKey(JumpDriveModel, on_delete=models.CASCADE)
	impulse_engine = models.ForeignKey(ImpulseEngineModel, on_delete=models.CASCADE)
	computer = models.ForeignKey(ComputerModel, on_delete=models.CASCADE)
	ship_type = models.ForeignKey(ShipTypeModel, on_delete=models.CASCADE)
	weapons = models.ManyToManyField(WeaponModel)
	ammunitions = models.ManyToManyField(AmmunitionModel)


class SubroutineModel(models.Model):
	subroutine_id = models.AutoField(primary_key=True, unique=True)
	ship = models.ForeignKey(ShipModel, on_delete=models.CASCADE)
	priority = models.IntegerField()


class ConditionModel(models.Model):
	condition_id = models.AutoField(primary_key=True, unique=True)
	name = models.CharField(max_length=100, choices=[('AL', 'AmmunitionLevel'), ('DI', 'Distance'), ('EL', 'EnergyLevel'), ('HE', 'Health'), ('ID', 'IsDisabled')])
	at_least = models.IntegerField(blank=True, null=True)
	at_most = models.IntegerField(blank=True, null=True)
	target = models.IntegerField(choices=[(0, 'SELF'), (1, 'ENEMY')], blank=True, null=True)
	component_name = models.CharField(blank=True, null=True, max_length=100)
	subroutine = models.ForeignKey(SubroutineModel, on_delete=models.CASCADE)


class ActionModel(models.Model):
	action_id = models.AutoField(primary_key=True, unique=True)
	name = models.CharField(max_length=100, choices=[('AR', 'AttemptRepairs'), ('DE', 'Delay'), ('FI', 'FireImpulse'), ('FW', 'FireWeapon'), ('JU', 'Jump'), ('SC', 'Scan')])
	subroutines = models.ForeignKey(SubroutineModel, on_delete=models.CASCADE)
	component_name = models.CharField(max_length=100, blank=True, null=True)
	ammunition_name = models.CharField(max_length=100, blank=True, null=True)
