from django.db import models


# Create your models here.
class ImpulseEngineModel(models.Model):
	impulse_engine_id = models.IntegerField(primary_key=True, unique=True)
	name = models.CharField(max_length=100, unique=True)
	mass = models.IntegerField()
	energy_cost = models.IntegerField()
	repair_cost = models.IntegerField()
	max_accel = models.IntegerField()
	
	def __str__(self):
		return self


class JumpDriveModel(models.Model):
	jump_drive_id = models.IntegerField(primary_key=True, unique=True)
	name = models.CharField(max_length=100, unique=True)
	mass = models.IntegerField()
	energy_cost = models.IntegerField()
	repair_cost = models.IntegerField()


class WeaponModel(models.Model):
	weapon_id: models.IntegerField(primary_key=True, unique=True)
	name = models.CharField(max_length=100, unique=True)
	mass = models.IntegerField()
	energy_cost = models.IntegerField()
	repair_cost = models.IntegerField()
	damage = models.IntegerField()
	munition_velocity = models.IntegerField()
	ammunition_type = models.IntegerField()


class RadarModel(models.Model):
	radar_id = models.IntegerField(primary_key=True, unique=True)
	name = models.CharField(max_length=100, unique=True)
	mass = models.IntegerField()
	energy_cost = models.IntegerField()
	repair_cost = models.IntegerField()
	tracking_styel = models.IntegerField()


class ArmourModel(models.Model):
	armour_id = models.IntegerField(primary_key=True, unique=True)
	name = models.CharField(max_length=100, unique=True)
	mass = models.IntegerField()
	repair_cost = models.IntegerField()
	armour_type = models.IntegerField()


class ShipTypeModel(models.Model):
	ship_type_id = models.IntegerField(primary_key=True, unique=True)
	name = models.CharField(max_length=100, unique=True)
	weight = models.IntegerField()
	power_gen = models.IntegerField()
	battery_max = models.IntegerField()


class AmmunitionModel(models.Model):
	ammunition_id = models.IntegerField(primary_key=True, unique=True)
	name = models.CharField(max_length=100, unique=True)
	mass = models.IntegerField()
	repair_cost = models.IntegerField()
	damage_type = models.IntegerField()
	ammunition_type = models.IntegerField()


class ComputerModel(models.Model):
	computer_id = models.IntegerField(primary_key=True, unique=True)
	name = models.CharField(max_length=100, unique=True)
	mass = models.IntegerField()
	repair_cost = models.IntegerField()
	speed = models.IntegerField()
	capacity = models.IntegerField()
