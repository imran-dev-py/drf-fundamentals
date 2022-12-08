from rest_framework import serializers
from . import models

"""
# https://www.django-rest-framework.org/api-guide/serializers/#validation
class EmployeeSerializers(serializers.Serializer):
	name = serializers.CharField(max_length=4) # in built validation
	no = serializers.IntegerField()
	salary = serializers.CharField()
	address = serializers.CharField()

	# object level validation [multiple fields validation at the same time]
	def validate(self, data):
		name = data['name'] or self.instance.name
		salary = data['salary'] or self.instance.salary
		print('object')

		if name.lower() == 'sunny':
			if int(data['salary']) < 15000:
				raise serializers.ValidationError('Sunny\'s salary should be 15000 & more')
		return data

	# field level validation [single validation]
	def validate_salary(self, value):
		print('field') # it's get called first
		if int(value) < 5000:
			raise serializers.ValidationError('Employee salary should not less than 5000')
		return value

	# for post request
	def create(self, validated_data):
		return models.Employee.objects.create(**validated_data)

	# for put/partial request
	def update(self, instance, validated_data):
		instance.name = validated_data.get('name', instance.name)
		instance.no = validated_data.get('no', instance.no)
		instance.salary = validated_data.get('salary', instance.salary)
		instance.address = validated_data.get('address', instance.address)
		instance.save()
		return instance
	
"""

class EmployeeSerializers(serializers.ModelSerializer):
	class Meta:
		model = models.Employee
		fields = '__all__'
		
