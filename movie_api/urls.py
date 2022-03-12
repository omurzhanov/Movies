from rest_framework.routers import DefaultRouter
from . import views
from django.urls import path
# router = DefaultRouter()
# router.register(r'movies', views.MovieViewSet, basename='movie')
urlpatterns = [
    path('movies/<int:pk>/', views.MovieDetailView.as_view()),
    path('movies/', views.MovieListView.as_view()),
]
