from django.shortcuts import render, HttpResponse
import json
from django.http import JsonResponse
from django.views import View
from .mixins import HttpResponseMixin

def employee_data_view(request):
	data = {
		'eno': 100,
		'ename': 'Sunny leone',
		'esal': 1000,
		'eaddr': 'Mumbai',
	}

	return HttpResponse(
		f'Number {data["eno"]} || ' 
		f'Name {data["ename"]} || '
		f'Salary {data["esal"]} || '
		f'Address {data["eaddr"]}'
	)


def emp_data_json_view(request):
	data = {
		'eno': 100,
		'ename': 'Sunny leone',
		'esal': 100000,
		'eaddr': 'Mumbai',
	}

	# convert dictionary to json
	json_data = json.dumps(data)
	# https://www.geeksforgeeks.org/what-is-the-correct-json-content-type/
	return HttpResponse(
		json_data, content_type='application/json'
	)


# without converting, directly send
def emp_data_json_view2(request):
	data = {
		'eno': 100,
		'ename': 'Sunny leone',
		'esal': 100000,
		'eaddr': 'Mumbai',
	}

	return JsonResponse(
		data
	)

class JsonCBV(View):
	def get(self, request, *args, **kwargs):
		data = {
			'eno': 100,
			'ename': 'Sunny leone',
			'esal': 100000,
			'eaddr': 'Mumbai',
		}

		return JsonResponse(data)

class JsonCBV2(HttpResponseMixin, View):
	def get(self, request, *args, **kwargs):
		data = {
			'eno': 100,
			'ename': 'Sunny leone',
			'esal': 100000,
			'eaddr': 'Mumbai',
		}

		json_data = json.dumps(data)
		return self.render_to_http_response(json_data)
