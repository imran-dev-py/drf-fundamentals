from django.shortcuts import render, HttpResponse
from . import models, forms
from django.views import View
import json
from django.core import serializers # https://docs.djangoproject.com/en/4.1/topics/serialization/
from .mixins import SerializeMixin

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .utilits import is_json, get_object_by_id

class EmployeeCURDOperation(SerializeMixin, View):
	def get(self, request, *args, **kwargs):
		json_string = request.body
		print(json_string)

		if not is_json(json_string):
			json_data = json.dumps({'message': 'Not Valid'})
			return HttpResponse(json_data, content_type='application/json')

		py_object = json.loads(json_string)
		id_ = py_object.get('id', None)

		if id_ is not None:
			employee = get_object_by_id(id_)
			if employee is None:
				json_data = json.dumps({'message': 'Not Available'})
				return HttpResponse(json_data, content_type='application/json')
			json_data = self.serializeData([employee,])
			return HttpResponse(json_data, content_type='application/json')
		
		employees = models.Employee.objects.all()
		json_data = self.serializeData([employees,])
		return HttpResponse(json_data, content_type='application/json')
"""
@method_decorator(csrf_exempt, name='dispatch')
class EmployeeDetails(SerializeMixin, View):
	def get(self, request, id, *args, **kwargs):
		try:
			employee = models.Employee.objects.get(id=id)
		except models.Employee.DoesNotExist:
			json_data = json.dumps({
				"msg": 'Not Found!'
			})
			return HttpResponse(json_data, content_type='application/json', status=404)
		else:
			json_data =  self.serializeData(employee)
			return HttpResponse(json_data, content_type='application/json')


		# json_data = serializers.serialize('json', [employee,], fields=('name', 'no', 'address'))
		# employee_data = {
		# 	'no': employee.no,
		# 	'name': employee.name, 
		# 	'salary': employee.salary,
		# 	'address': employee.address,
		# }
		# json_data = json.dumps(employee_data)
		# return HttpResponse(json_data, content_type='application/json')
		# return self.serializeData(employee)

	def put(self, request, id, *args, **kwargs):
		employee = get_object_by_id(id)

		if employee is None:
			json_data = json.dumps({
				'msg': 'Invalid Id request',
			})
			return HttpResponse(json_data, content_type='application/json')
		
		data = request.body
		if not is_json(data):
			json_data = json.dumps({
				'msg': 'send valid json data'
			})
			return HttpResponse(json_data, content_type='application/json')

		employee_data = json.loads(data)
		original_data = {
			'name': employee.name,
			'no': employee.no,
			'salary': employee.salary,
			'address': employee.address
			}
		original_data.update(employee_data)
		form = forms.EmployeeForm(original_data, instance=employee)

		if form.is_valid():
			form.save(commit=True)
			json_data = json.dumps({'msg': 'updated successfully'})
			return HttpResponse(json_data, content_type='application/json')

		if form.errors:
			json_data = json.dumps(form.errors)
			return HttpResponse(json_data, content_type='application/json')

	def delete(self, request, id, *args, **kwargs):
		employee = get_object_by_id(id)

		if employee is None:
			json_data = json.dumps({'msg': 'Invalid id request'})
			return HttpResponse(json_data, content_type='application/json')

		status, deleted_item = employee.delete() # return tuple(status=1, Itemobject={'app.Object=1'})
		if status == 1:
			json_data = json.dumps({'msg': 'Deleted successfully'})
			return HttpResponse(json_data, content_type='application/json')
		else:
			json_data = json.dumps({'msg': 'Something is wrong, try again'})
			return HttpResponse(json_data, content_type='application/json')


# without mixin
@method_decorator(csrf_exempt, name='dispatch')
class EmployeeList(View):
	def get(self, request, *args, **kwargs):
		json_data = serializers.serialize('json', models.Employee.objects.all())
		data = json.loads(json_data)

		database_data = []
		for objKey in data:
			database_data.append(objKey["fields"])

		return HttpResponse(json.dumps(database_data, indent=1), content_type='application/json')

	def post(sefl, request, *args, **kwargs):
		data = request.body
		is_data_valid = is_json(data)

		if not is_data_valid:
			json_data = json.dumps({
				'msg': 'send valid json data'
			})
			return HttpResponse(json_data, content_type='application/json')

		employee_data = json.loads(data) # dict
		form = forms.EmployeeForm(employee_data)

		if form.is_valid():
			form.save(commit=True)
			json_data = json.dumps({'msg': 'added successfully'})
			return HttpResponse(json_data, content_type='application/json')

		if form.errors:
			json_data = json.dumps(form.errors)
			return HttpResponse(json_data, content_type='application/json')
"""