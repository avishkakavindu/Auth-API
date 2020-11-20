from django.urls import path, include
from api2 import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('students', views.StudentViewSet )

urlpatterns = [
    path('', include(router.urls), name='students'),
]

"""
urlpatterns = [
    path('students', views.StudentList.as_view(), name='studentlist'),
    path('students/<int:pk>', views.StudentDetail.as_view(), name='studentdetail'),
]
"""
