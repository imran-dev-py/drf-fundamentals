from django.urls import path 
from hello import views

urlpatterns = [
	path('api/', views.EmployeeCurd.as_view(), name='details')
]