from django.urls import path 
from . import views

urlpatterns = [
	path('', views.employee_data_view, name='data'),
	path('json/', views.emp_data_json_view, name='json'),
	path('jj/', views.emp_data_json_view2, name='jj'),
	path('cv-json/', views.JsonCBV.as_view(), name='cv-json'),
	path('cc/', views.JsonCBV2.as_view(), name='cc')
]