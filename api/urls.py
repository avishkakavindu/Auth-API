from django.urls import path
from api import views


urlpatterns = [
    path('students/', views.student_list, name='students'),
    path('students/<int:pk>', views.student_detail, name='student_detail'),
]