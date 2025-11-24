from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_video, name='add_video'),
    path('view/<int:movie_id>/', views.view_video, name='view_video'),
    path('update/<int:movie_id>/', views.update_video, name='update_video'),
    path('delete/<int:movie_id>/', views.delete_video, name='delete_video'),
]