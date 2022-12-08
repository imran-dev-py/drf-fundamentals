import requests, json

URL = 'http://127.0.0.1:8000/api'

def get_data(id):
	response = requests.get(f'{URL}/{id}/')
	if response.status_code != 200:
		print('Invalid request, try again')
	else:
		employee_info = response.json()
		print(response.status_code)
		print(employee_info)

# get_data(400)

# fetch all data
def get_all_data():
	response = requests.get(f'{URL}/all/')
	employee_infos = response.json()
	print(response.status_code)
	pprint(employee_infos)

# get_all_data()

def create_data():
	new_emp = {
		'name': 'Lisa Falcon',
		'no': 500,
		'salary': 5000,
		'address': 'LA, California'
	}

	response = requests.post(f'{URL}/all/', data=json.dumps(new_emp))
	print(response.status_code)
	print(response.json()) # dict

# create_data()

def update_resource(id):
	emp = {
		'name': 'Leya Falcon',
	}
	response = requests.put(f'{URL}/{id}/', data=json.dumps(emp))
	if response.status_code != 200:
		print('Match Id not found')
	else:
		print(response.status_code)
		print(response.json()) # dict

update_resource(5)

def delete_resource(id):
	response = requests.delete(f'{URL}/{id}/')
	if response.status_code != 200:
		print('Match Id not found')
	else:
		print(response.status_code)
		print(response.json()) # dict

# delete_resource(11)
