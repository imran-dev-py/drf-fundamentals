import json
from . import models




def is_json(data):
	try:
		py_object = json.loads(data)
		is_validated = True 
	except ValueError as e:
		is_validated = False
	
	return is_validated



def get_object_by_id(id):
	try:
		employee = models.Employee.objects.get(id=id)
	except Employee.DoesNotExist as e:
		employee = None 

	return employee

