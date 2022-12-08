from django.urls import path 
from . import views

urlpatterns = [
	path('api/', views.EmployeeListAPIView.as_view(), name='employee'),
	path('api2/', views.EmployeeListAPI.as_view(), name='employee2'),
	
	path('api3/', views.EmployeeCreateApiView.as_view(), name='employee3'),
]