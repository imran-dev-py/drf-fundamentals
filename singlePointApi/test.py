import requests
import json 

URL = 'http://127.0.0.1:8000/api/'

def fetch_data(id=None):
	x = {}
	if id is not None:
		x = {'id': id}

	response = requests.get(URL, data=json.dumps(x))
	print(response.status_code)

# fetch_data(2)

def add_data():
	new_star = {
		'name': 'Kristy Black',
		'rank': 5,
		'salary': 25000,
		'address': 'Prag, Czeck Republic'
	}

	response = requests.post(URL, data=json.dumps(new_star))
	print(response.status_code)

# add_data()

def update_data(id):
	data = {
		'address': 'Sao Paulo, Brazil',
		'id': id,
	}
		
	response = requests.put(URL, data=json.dumps(data))
	print(response.status_code)

# update_data(2)

def delete_resource(id):
	response = requests.delete(URL, data=json.dumps({'id': id}))
	print(response.status_code)

delete_resource(2)