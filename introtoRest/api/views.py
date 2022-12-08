from django.shortcuts import render, HttpResponse
from django.views import View
import json
from . import serializers, models

import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

@method_decorator(csrf_exempt, name='dispatch')
class EmployeeCURD(View):
	def get(self, request, *args, **kwargs):
		json_string = request.body 
		print(json_string)

		stream = io.BytesIO(json_string)
		json_to_dict = JSONParser().parse(stream)

		get_id = json_to_dict.get('id', None)
		if get_id is None:
			employees = models.Employee.objects.all()
			model_to_dict = serializers.EmployeeSerializers(employees, many=True)
			json_data = JSONRenderer().render(model_to_dict.data)
			return HttpResponse(json_data, content_type='application/json')

		employee = models.Employee.objects.get(id=get_id)
		model_to_dict = serializers.EmployeeSerializers(employee)
		json_data = JSONRenderer().render(model_to_dict.data)
		return HttpResponse(json_data, content_type='application/json')

	def post(self, request, *args, **kwargs):
		json_string = request.body

		stream = io.BytesIO(json_string)
		parse_into_dict = JSONParser().parse(stream)

		serializer = serializers.EmployeeSerializers(data=parse_into_dict)
		if serializer.is_valid():
			serializer.save()
			message = {
				'msg': 'Added Successfully'
			}
			render_into_json = JSONRenderer().render(message)
			return HttpResponse(render_into_json, content_type='application/json')

		if serializer.errors:
			render_into_json = JSONRenderer().render(serializer.errors)
			return HttpResponse(render_into_json, content_type='application/json')

	def put(self, request, *args, **kwargs):
		json_string = request.body

		stream = io.BytesIO(json_string)
		parse_into_dict = JSONParser().parse(stream)

		get_id = parse_into_dict.get('id', None)
		if get_id is None:
			json_data = json.dumps({'message': 'Invalid Id request'})
			return HttpResponse(parse_inti_json, content_type='application/json')

		employee = models.Employee.objects.get(id=get_id)
		serializer = serializers.EmployeeSerializers(employee, data=parse_into_dict, partial=True)
		
		if serializer.is_valid():
			 # internally get called update() method in serializers.py
			serializer.save()
			message = {
				'msg': 'Updated Successfully'
			}
			render_into_json = JSONRenderer().render(message)
			return HttpResponse(render_into_json, content_type='application/json')

		if serializer.errors:
			render_into_json = JSONRenderer().render(serializer.errors)
			return HttpResponse(render_into_json, content_type='application/json')

	def delete(self, request, *args, **kwargs):
		json_string = request.body 

		stream = io.BytesIO(json_string)
		parse_into_dict = JSONParser().parse(stream)

		get_id = parse_into_dict.get('id', None)
		employee = models.Employee.objects.get(id=get_id)
		employee.delete()
		json_data = json.dumps({'message': 'Deleted successfully'})
		return HttpResponse(json_data, content_type='application/json')





