from django.shortcuts import render, HttpResponse
from django.core import serializers
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from . import models, forms, mixins, utilits
from django.views import View

import json

@method_decorator(csrf_exempt, name='dispatch')
class StudentCURDView(View):
	def get(self, request, *args, **kwargs):
		json_string = request.body
		print(json_string)

		if not utilits.valid_json(json_string):
			json_data = json.dumps({'message': 'Invalid Json Data'})
			return HttpResponse(json_data, content_type='application/json')

		json_to_dict = json.loads(json_string)
		student_id = json_to_dict.get('id', None)

		if student_id is None:
			students = models.Student.objects.all()
			json_data = serializers.serialize('json', students)
			return HttpResponse(json_data, content_type='application/json')

		student = utilits.get_object_by_id(student_id)

		if student is None:
			json_data = json.dumps({'message': 'Requested Information not found'})
			return HttpResponse(json_data, content_type='application/json')

		json_data = serializers.serialize('json', [student,])
		return HttpResponse(json_data, content_type='application/json')

	def post(self, request, *args, **kwargs):
		json_string = request.body
		print(json_string)

		if not utilits.valid_json(json_string):
			json_data = json.dumps({'message': 'Invalid Json Data'})
			return HttpResponse(json_data, content_type='application/json')

		json_to_dict = json.loads(json_string)

		form = forms.StudentForm(json_to_dict)
		if form.is_valid():
			form.save()
			json_data = json.dumps({'message': 'Added Successfully'})
			return HttpResponse(json_data, content_type='application/json')

		if form.errors:
			return HttpResponse(json.dumps(form.errors), content_type='application/json')

	def put(self, request, *args, **kwargs):
		json_string = request.body

		if not utilits.valid_json(json_string):
			json_data = json.dumps({'message': 'Invalid Json Data'})
			return HttpResponse(json_data, content_type='application/json')

		update_data = json.loads(json_string)
		get_id = update_data.get('id', None)

		if get_id is None:
			json_data = json.dumps({'message': 'We cant update information with this requested ID'})
			return HttpResponse(json_data, content_type='application/json')

		student = utilits.get_object_by_id(get_id)
		if student is None:
			return HttpResponse(json.dumps({'message': 'Requested Student information not found to update'}), content_type='application/json')

		original_data = {
			'name': student.name,
			'roll': student.roll,
			'marks': student.marks,
			'gf': student.gf,
			'bf': student.bf,
		}
		original_data.update(update_data)
		form = forms.StudentForm(original_data, instance=student)

		if form.is_valid():
			form.save()
			json_data = json.dumps({'message': 'Updated Successfully'})
			return HttpResponse(json_data, content_type='application/json')

		if form.errors:
			return HttpResponse(json.dumps(form.errors), content_type='application/json')

	def delete(self, request, *args, **kwargs): 
		data = request.body 

		if not utilits.valid_json(data):
			json_data = json.dumps({'message': 'Invalid Json Data'})
			return HttpResponse(json_data, content_type='application/json')

		json_to_dict = json.loads(data)
		get_id = json_to_dict.get('id', None)

		if get_id is None:
			json_data = json.dumps({'message': 'We cant delete information with this requested "None"'})
			return HttpResponse(json_data, content_type='application/json')

		student = utilits.get_object_by_id(get_id)
		if student is None:
			return HttpResponse(json.dumps({'message': 'Requested Student information not found to delete'}), content_type='application/json')
		status, deleted_object = student.delete()
		if status == 1:
			return HttpResponse(json.dumps({'message': 'Requested Information deleted Successfully'}), content_type='application/json') 
		return HttpResponse(json.dumps({'message': 'Something is wrong, try again'}), content_type='application/json')




