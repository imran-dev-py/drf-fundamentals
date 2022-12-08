from django.urls import path
from . import views 

urlpatterns = [
	path('', views.EmployeeCURD.as_view())
]