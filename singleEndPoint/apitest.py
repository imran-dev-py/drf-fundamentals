import requests
import json

URL = 'http://127.0.0.1:8000/api/'

def student_info(id=None):
	dict_to_json = {}

	if id is not None:
		dict_to_json['id'] = id 

	response = requests.get(URL, data=json.dumps(dict_to_json))
	print(response.json())
	print(response.status_code)

# student_info()

def add_student():
	new_student = {
		'name': 'Dhoni',
		'marks': 100,
		'roll': 154,
		'gf': 'Sunny',
		'bf': 'Itself',
	}

	response = requests.post(URL, data=json.dumps(new_student))
	print(response.json())
	print(response.status_code)

# add_student()

def update_info(id=None):
	response = requests.put(URL, data=json.dumps({'id': id, 'bf': 'Hero Alam'}))
	print(response.json()['message'])
	print(response.status_code)

# update_info(1)

def delete_info(id=None):
	response = requests.delete(URL, data=json.dumps({'id': id}))
	print(response.status_code)
	print(response.json()['message'])
	

delete_info()