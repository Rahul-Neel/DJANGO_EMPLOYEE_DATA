from django.urls import path
from . import views

urlpatterns =[
    path('<int:pk>/',views.employee_details,name='emp_data'),
]