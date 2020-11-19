from django.urls import path
from api2 import views


urlpatterns = [
    path('students', views.StudentList.as_view(), name='studentlist'),
    path('students/<int:pk>', views.StudentDetail.as_view(), name='studentdetail'),

]
