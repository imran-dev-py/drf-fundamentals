import requests
import json 

URL = 'http://localhost:8000/api/'

def get_data(id=None):
	data = {}

	if id is not None:
		data = {'id': id}

	response = requests.get(URL, data=json.dumps(data))
	print(response.status_code)
	print(response.json())

# get_data()

def add_data():
	new_model_instance = {
		'name': 'Francis Belle', 
		'no': 700,
		'salary': 44020,
		'address': 'Sao Paulo'
	}

	response = requests.post(URL, data=json.dumps(new_model_instance))
	print(response.status_code)
	print(response.json())

# add_data()

def update_data(id):
	data = {
		'address': 'Sao Paulo, Brazil',
	}
	data['id'] = id

	response = requests.put(URL, data=json.dumps(data))
	print(response.status_code)
	print(response.json())

# update_data(id=7)

def delete_data(id):
	data = {'id': id}

	response = requests.delete(URL, data=json.dumps(data))
	print(response.status_code)
	print(response.json())

# delete_data(1)