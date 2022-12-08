from django.shortcuts import render, HttpResponse
import json
from . import models, mixins, forms
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.views import View

def valid_json(data):
	try:
		is_valid = True 
		json_to_dict = json.loads(data)
	except ValueError as error:
		is_valid = False
	return is_valid

def get_object_by_id(id):
	try:
		single_query = models.Employee.objects.get(id=id)
	except models.Employee.DoesNotExist as e:
		single_query = None

	return single_query


@method_decorator(csrf_exempt, name='dispatch')
class EmployeeCurd(mixins.SerializeMixin, View):
	def get(self, request, *args, **kwargs):
		json_string = request.body
		print(json_string)

		if not valid_json(json_string):
			json_data = {
				'message': 'Not valid json'
			}
			return HttpResponse(json.dumps(json_data), content_type='application/json')

		json_to_dict = json.loads(json_string)
		id_ = json_to_dict.get('id', None)

		if id_ is not None:
			employee = get_object_by_id(id)
			if employee is None:
				json_data = {'message': 'Object not found'}
				return HttpResponse(json.dumps(json_data), content_type='application/json')

			# return HttpResponse(self.serializeData(employee), content_type='application/json')
			return self.serializeData(employees)

		if id_ is None:
			employees = models.Employee.objects.all()
			return self.serializeData(employees)

	def post(self, request, *args, **kwargs):
		data = request.body

		if not valid_json(data):
			json_data = {
				'message': 'Not valid json'
			}
			return HttpResponse(json.dumps(json_data), content_type='application/json')

		json_to_dict = json.loads(data)
		form = forms.EmployeeForm(json_to_dict)

		if form.is_valid():
			form.save()
			json_data = json.dumps({'messae': 'Added successfully'})
			return HttpResponse(json_data, content_type='application/json')

		if form.error:
			return HttpResponse(json.dumps(form.errors), content_type='application/json')

	def put(self, request, *args, **kwargs):
		data = request.body

		if not valid_json(data):
			json_data = {
				'message': 'Not valid json'
			}
			return HttpResponse(json.dumps(json_data), content_type='application/json')

		json_to_dict = json.loads(data)
		id_ = json_to_dict.get('id', None)

		if id_ is None:
			json_data = {
				'message': 'Not valid Id'
			}
			return HttpResponse(json.dumps(json_data), content_type='application/json')

		employee = get_object_by_id(id)
		if employee is None:
			json_data = json.dumps({
				'msg': 'Invalid Id request',
			})
			return HttpResponse(json_data, content_type='application/json')

		provided = json.loads(data)
		original_data = {
			'name': employee.name,
			'rank': employee.rank,
			'salary': employee.salary,
			'address': employee.address,
		}
		original_data.update(provided)

		form = forms.EmployeeForm(original_data,instance=employee)

		if form.is_valid():
			form.save(commit=True)
			json_data = json.dumps({'msg': 'updated successfully'})
			return HttpResponse(json_data, content_type='application/json')

		if form.errors:
			json_data = json.dumps(form.errors)
			return HttpResponse(json_data, content_type='application/json')

	def delete(self, request, *args, **kwargs):
		data = request.body

		if not valid_json(data):
			json_data = {
				'message': 'Not valid json'
			}
			return HttpResponse(json.dumps(json_data), content_type='application/json')

		json_to_dict = json.loads(data)
		id_ = json_to_dict.get('id', None)

		if id_ is None:
			json_data = json.dumps({
					'msg': 'Invalid Id request',
				})
			return HttpResponse(json_data, content_type='application/json')
			

		if id_ is not None:
			employee = get_object_by_id(id)
			if employee is None:
				json_data = json.dumps({
					'msg': 'Invalid Id request',
				})
				return HttpResponse(json_data, content_type='application/json')
			
		status, deleted_item = employee.delete()
		if status == 1:
			json_data = json.dumps({'msg': 'Deleted successfully'})
			return HttpResponse(json_data, content_type='application/json')
		else:
			json_data = json.dumps({'msg': 'Something is wrong, try again'})
			return HttpResponse(json_data, content_type='application/json')





