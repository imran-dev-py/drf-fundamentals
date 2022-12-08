from django.shortcuts import render, HttpResponse
from . import models, serializers

from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, CreateAPIView

class EmployeeListAPIView(APIView):
	def get(self, request, format=None):
		employees = models.Employee.objects.all()
		# queryset to dict
		serializer = serializers.EmployeeSerializer(employees, many=True).data
		# dict to json
		return Response(serializer)

	def post(self, request):
		serializer = serializers.EmployeeSerializer(data=request.data)

		if serializer.is_valid():
			name = serializers.data.get('name')
			return Response({'message': f'Hello {name}'})

		if serializer.errors:
			return Response(serializer.errors)

# predefined display view
class EmployeeListAPI(ListAPIView):
	# queryset = models.Employee.objects.all()
	serializer_class = serializers.EmployeeSerializer

	def get_queryset(self):
		queryset = models.Employee.objects.all()
		address = self.request.GET.get('address')

		if address is not None:
			new_queryset = queryset.filter(address__icontains=address)
			return new_queryset

class EmployeeCreateApiView(CreateAPIView):
	queryset = models.Employee.objects.all()
	serializer_class = serializers.EmployeeSerializer