from django.db import models

class Employee(models.Model):
	name = models.CharField(max_length=50)
	no = models.IntegerField()
	salary = models.CharField(max_length=50)
	address = models.CharField(max_length=500)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Employee'
		verbose_name_plural = 'Employees'