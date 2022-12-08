from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response # converts dict to json

from . import serializers

class TestAPIView(APIView):
	def get(self, request):
		colors = ['RED', 'YELLOW', 'GREEN', 'BLUE', 'BLACK', 'WHITE']
		return Response({
			'message': 'Happy Pongal',
			'colors': colors,
		})

	def post(self, request):
		serializer = serializers.NameSerializer(data=request.data)

		if serializer.is_valid():
			name = serializer.data.get('name')
			return Response({
				'message': f'Hello {name}, Happy Pongal'
			})
		if serializer.errors:
			return Response(serializer.errors)
	
	def put(self, request):
		return Response({'message': 'From Put request'})

	def delete(self, request):
		return Response({'message': 'From delete request'})

	def patch(self, request):
		return Response({'message': 'From patch request'})

class TestViewSet(ViewSet):
	def list(self, request):
		colors = ['RED', 'YELLOW', 'GREEN', 'BLUE', 'BLACK', 'WHITE']
		return Response({
			'message': 'Happy Pongal',
			'colors': colors,
		})

	def create(self, request):
		serializer = serializers.NameSerializer(data=request.data)

		if serializer.is_valid():
			name = serializer.data.get('name')
			return Response({
				'message': f'Hello {name}, Happy Pongal'
			})
		if serializer.errors:
			return Response(serializer.errors)

	def update(self, request, pk=None):
		return Response({'message': 'From update request'})

	def destroy(self, request, pk=None):
		return Response({'message': 'From destroy request'})

	def partial_update(self, request, pk=None):
		return Response({'message': 'From patch request'})

	def retrieve(self, request, pk=None):
		return Response({'message': 'From retrieve request'})
