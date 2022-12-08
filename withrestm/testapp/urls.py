from django.urls import path 
from . import views 


urlpatterns = [
	# path('<int:id>/', views.EmployeeDetails.as_view(), name='details'),
	# path('all/', views.EmployeeList.as_view(), name='all-info')
	path('api/', views.EmployeeCURDOperation.as_view(), name='curd-operation')
]