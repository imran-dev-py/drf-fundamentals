import json
from . import models

def valid_json(json_string):
	try:
		is_valid = True
		json_to_dict = json.loads(json_string)
	except ValueError as error:
		is_valid = False

	return is_valid

def get_object_by_id(id):
	try:
		single_query = models.Student.objects.get(id=id)
	except models.Student.DoesNotExist as error:
		single_query = None

	return single_query
