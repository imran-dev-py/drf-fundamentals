from django.db import models


class Employee(models.Model):
	name = models.CharField(max_length=65)
	ra = models.IntegerField()
	salary = models.FloatField()
	address = models.CharField(max_length=100)

	def __str__(self):
		return self.name 

	class Meta:
		verbose_name_plural = 'Employees'
		verbose_name = 'Employee'

	