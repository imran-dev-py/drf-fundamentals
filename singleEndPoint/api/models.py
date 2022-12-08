from django.db import models

class Student(models.Model):
	name = models.CharField(max_length=200)
	marks = models.IntegerField()
	roll = models.IntegerField()
	gf = models.CharField(max_length=200)
	bf = models.CharField(max_length=50)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Student'
		verbose_name_plural = 'Students'
