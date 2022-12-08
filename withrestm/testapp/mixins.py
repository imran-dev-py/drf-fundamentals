from django.core import serializers
import json
from django.shortcuts import HttpResponse

class SerializeMixin(object):
	def serializeData(self, queryData):
		json_data = serializers.serialize('json', [queryData,])
		data = json.loads(json_data)

		database_data = []
		for objKey in data:
			database_data.append(objKey["fields"])

		return HttpResponse(json.dumps(database_data, indent=1), content_type='application/json')
