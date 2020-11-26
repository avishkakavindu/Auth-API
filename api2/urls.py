from django.urls import path, include
from api2 import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('author/', views.AuthorListView.as_view(), name='authorlist'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='authordetail'),
    path('book/', views.BookListView.as_view(), name='booklist'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='bookdetail'),
]

